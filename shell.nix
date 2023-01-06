{ sources ? import ./nix/sources.nix
, pkgs ? import sources.nixpkgs { }
}:

pkgs.mkShell {

  buildInputs = [
    pkgs.python310Full
    pkgs.poetry
    pkgs.sphinx
  ];

}
