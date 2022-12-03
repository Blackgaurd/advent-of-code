function main()
    io = open("day2/input.txt")

    win = Dict(
        "Y" => "A" ,
        "Z" => "B" ,
        "X" => "C" ,
    )
    same = Dict(
        "A"=>"X",
        "B"=>"Y",
        "C"=>"Z",
    )
    points = Dict(
        "X"=> 1,
        "Y"=> 2,
        "Z"=> 3,
    )

    total = 0
    for line in eachline(io)
        a, b = split(line, " ")
        total += points[b]
        if win[b] == a
            total += 6
        elseif same[a] == b
            total += 3
        end
    end

    println(total)

    close(io)
end

main()