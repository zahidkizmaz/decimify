{
  description = "decimify flake";

  inputs = {
    flake-parts.url = "github:hercules-ci/flake-parts";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    inputs@{ flake-parts, ... }:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      perSystem =
        { pkgs, system, ... }:
        let
          python313 = pkgs.python313.withPackages (ps: with ps; [ uv ]);
        in
        {
          devShells.default = pkgs.mkShell {
            buildInputs = [ python313 ];
            UV_PYTHON = "${python313}/bin/python";
            shellHook = ''
              if [ ! -d .venv ]; then
                echo "Creating virtual environment..."
                uv sync
              fi
              source .venv/bin/activate
            '';
          };
        };
    };
}
