function main()
    io = open("day2/input.txt")

    total = 0
    for line in eachline(io)
        a, b = split(line, " ")
        if b == "X"
            # lose
            points = Dict(
                "A"=>3,
                "B"=>1,
                "C"=>2,
            )
            total += points[a]
        elseif b == "Y"
            # draw
            total += 3
            points = Dict(
                "A"=>1,
                "B"=>2,
                "C"=>3,
            )
            total += points[a]
        elseif b == "Z"
            # win
            total += 6
            points = Dict(
                "A"=>2,
                "B"=>3,
                "C"=>1,
            )
            total += points[a]
        end
    end

    println(total)

    close(io)
end

main()