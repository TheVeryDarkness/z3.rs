with open("prebuild.yml", "w") as f:
    PLATFORM = [
        ["ubuntu-latest", "x64-linux", "libz3.a"],
        ["macos-latest", "x64-osx", "libz3.a"],
        ["windows-latest", "x64-windows-static-md", "libz3.lib"],
    ]
    f.write("""\
name: Upload prebuilt Z3
on:
  push:
    branches: [ upload-prebuilt-static-z3 ]
jobs:
  release:
    name: Create Release
    runs-on: ubuntu-latest
    env:
      VCPKG_ROOT: ${{ github.workspace }}/vcpkg
      VCPKG_REVISION: 5c82f7e6372c9b0ea25e1fd829dd50235ef37629
    steps:
      - name: Create Release
        id: create_release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: ${{ github.ref }}
          draft: false
          prerelease: false
      - uses: actions/checkout@v4
        with:
          submodules: recursive""")
    for os, triplet, _ in PLATFORM:
      f.write("""
      - name: vcpkg build z3
        uses: johnwason/vcpkg-action@v5
        with:
          pkgs: z3
          triplet: """+triplet+"""
          cache-key: """+os+"""
          revision: ${{ env.VCPKG_REVISION }}
          token: ${{ github.token }}
          extra-args: --clean-buildtrees-after-build""")
    f.write(f"""
      - name: prepare artifact
        run: |""")
    for _, triplet, lib in PLATFORM:
      f.write("""
          sh z3-sys/scripts/make_artifact.sh ${{ github.workspace }} ${{ env.VCPKG_ROOT }} """ + f"{triplet} {lib}")
    for _, triplet, _ in PLATFORM:
        f.write("""
      - name: upload artifact
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ github.token }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: ${{ github.workspace }}/x64-linux.tar.gz
          asset_name: x64-linux.tar.gz
          asset_content_type: application/gzip
        """)