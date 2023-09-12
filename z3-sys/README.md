# z3-sys

[![](https://img.shields.io/crates/v/z3-sys.svg)](https://crates.io/crates/z3-sys)

Low-level rust bindings to the Z3 SMT solver

Licensed under the MIT license.

See [https://github.com/Z3Prover/z3](https://github.com/Z3Prover/z3) for details on Z3.

## Documentation

The API is fully documented with examples:
[https://docs.rs/z3-sys/](https://docs.rs/z3-sys/)

## Installation

This crate works with Cargo and is on
[crates.io](https://crates.io/crates/z3-sys).
Add it to your `Cargo.toml` like so:

```toml
[dependencies]
z3-sys = "0.8"
```

**Note:** This crate requires a `z3.h` during build time.

* By default, the crate will look for a `z3.h` in standard/system include paths.
* If the feature `static-link-z3` is enabled, the `z3.h` of the built Z3 will be used.
* Alternatively, the path to the desired `z3.h` can be specified via the environment variable
`Z3_SYS_Z3_HEADER`. I.e., running:

  ```console
  $ Z3_SYS_Z3_HEADER="/path/to/my/z3.h" cargo build
  ```

  in your project will use `/path/to/my/z3.h` instead.

  By the way, using Cargo config (see [Environment variables](https://doc.rust-lang.org/cargo/  reference/config.html#environment-variables)) is also available.

* And the path to `z3.lib` or `libz3.lib` can also be specified via an environment variable `Z3_SYS_Z3_LIB`. I.e., running:

  ```console
  $ Z3_SYS_Z3_LIB="/path/to/my/z3/lib" cargo build
  ```

  in your project will ask the linker to search for `/path/to/my/z3/lib` instead.

  Otherwise, on Windows, it searches for `libz3.lib`, while on other os, it searches for `z3.lib`.

* If the feature `vcpkg` is enabled, it will use the z3 installed with [vcpkg](https://vcpkg.io).

  And it's done with a crate [vcpkg-rs](https://crates.io/crates/vcpkg). You may need to refer to it to know about how to configure them. For example, you may need to install vcpkg on your machine.

  On windows, [vcpkg-rs](https://crates.io/crates/vcpkg) uses `x64-windows-static-md` by default, while [vcpkg](https://vcpkg.io) uses `x64-windows-static` by default.

  It may be a feature that when using dynamically built z3, doctests can't find the dynamic library (for example, `libz3.so` or `libz3.dll`).
  
* There are many reasons to use statically built z3, though prebuilt binary by upstream repository [z3](https://github.com/Z3Prover/z3) only provide dynamic library.

  There's [an issue](https://github.com/Z3Prover/z3/issues/6897) for it.

## Support and Maintenance

I am developing this library largely on my own so far. I am able
to offer support and maintenance, but would very much appreciate
donations via [Patreon](https://patreon.com/endoli). I can also
provide commercial support, so feel free to
[contact me](mailto:bruce.mitchener@gmail.com).

## Contribution

Unless you explicitly state otherwise, any contribution
intentionally submitted for inclusion in the work by you,
shall be dual licensed as above, without any additional
terms or conditions.
