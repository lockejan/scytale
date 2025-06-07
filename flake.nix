{
  description = "Application packaged using poetry2nix";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, poetry2nix }:
    let
      system = "aarch64-darwin";
      pkgs = nixpkgs.legacyPackages.${system};

      p2n = poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };

      package = "scytale";
    in
    {
      # This block describes the build instructions for the default pkg
      packages.${system}.default = p2n.mkPoetryApplication {
        projectDir = ./.; # self also works here
      };

      # This block describes the default devShells
      # can be invoked via `nix develop`
      # makeShellNoCC gives a environment without C-Compiler
      devShells.${system}.default = pkgs.mkShellNoCC {

        # This will add our package to the dev environment
        packages = with pkgs; [
          # creates and enters a poetry environment
          (p2n.mkPoetryEnv {
            projectDir = ./.;
          })
          poetry
          sphinx
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
