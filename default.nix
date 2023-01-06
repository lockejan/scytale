{ sources ? import ./nix/sources.nix
, pkgs ? import sources.nixpkgs { }
}:
pkgs.poetry2nix.mkPoetryApplication {
  projectDir = ./.;
}
