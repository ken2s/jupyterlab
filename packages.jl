using Pkg
# Add julia packages to install like comments below when building the container image
#Pkg.add("ArgParse")
#Pkg.add(PackageSpec(url="https://github.com/staticfloat/InfluxDB.jl", rev="master"))

# Run `julia packages.jl` to install packages above
Pkg.update()
Pkg.add("BlackBoxOptim")
Pkg.add("CSV")
Pkg.add("DataFrames")
Pkg.add("Gadfly")
Pkg.add("GR")
Pkg.add("Latexify")
Pkg.add("LaTeXStrings")
Pkg.add("LinearAlgebra")
Pkg.add("Optim")
Pkg.add("Plots")
Pkg.add("Polynomials")
Pkg.add("PyPlot")
Pkg.add("RDatasets")
Pkg.add("SpecialFunctions")
Pkg.add("SpecialPolynomials")
Pkg.add("Statistics")
Pkg.add("WriteVTK")
