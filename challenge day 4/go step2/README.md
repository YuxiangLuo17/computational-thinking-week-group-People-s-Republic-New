
# Hello Go (VS Code ready)

This is a minimal Go "Hello World" project set up for VS Code.

## Run from VS Code
1. Open **VS Code** → **File → Open Folder...** → select this `hello-go` folder.
2. If prompted, install the **Go** extension (publisher: Go Team at Google) and tools.
3. Press **Ctrl+F5** to run (or **F5** to debug). You should see `Hello, World!` in the debug console/terminal.

## Run from terminal
```bash
go run .
```
or
```bash
go run main.go
```

## Common issues
- If you see `The system cannot find the file specified`, ensure you run the command **inside** this folder and that `main.go` exists here.
- Ensure your Go installation is on PATH: `go version` should print a version.
