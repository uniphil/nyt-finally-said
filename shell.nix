with import <nixpkgs> {};
with pkgs.python27Packages;

stdenv.mkDerivation {
  name = "python";

  buildInputs = [
    python36Full
  ];
}
