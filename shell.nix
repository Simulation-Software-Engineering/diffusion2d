{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
   python39
   python39Packages.numpy
   python39Packages.matplotlib
   python39Packages.build
   python39Packages.twine
  ];
}
