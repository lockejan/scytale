{
  description = "Application packaged using poetry2nix";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "aarch64-darwin";
      pkgs = nixpkgs.legacyPackages.${system};
      package = "scytale";
    in
    {
      # This block describes the build instructions for the default pkg
      packages.${system}.default = pkgs.poetry2nix.mkPoetryApplication {
        projectDir = ./.; # self also works here
      };

      # This block describes the default devShells
      # can be invoked via `nix develop`
      # makeShellNoCC gives a environment without C-Compiler
      devShells.${system}.default = pkgs.mkShellNoCC {

        # This will add our package to the dev environment
        packages = with pkgs; [
          # creates and enters a poetry environment
          (poetry2nix.mkPoetryEnv { projectDir = ./.; })
        ];
      };

      # if we comment this block we will yield the same result
      # because this is the default execution path for `nix build`
      apps.${system}.default = {
        program = "${self.packages.${system}.default}/bin/${package}";
        type = "app";
      };
    };
}
