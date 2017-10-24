with import <nixpkgs> {};
with pkgs.python27Packages;

stdenv.mkDerivation {
  name = "python";

  buildInputs = [
    pip
    python36Full
    virtualenv
  ];

  shellHook = ''
    SOURCE_DATE_EPOCH=$(date +%s)  # so that we can use python wheels
    virtualenv -p $(type -p python3) venv > /dev/null
    export PATH=$PWD/venv/bin:$PATH > /dev/null
  '';
}
