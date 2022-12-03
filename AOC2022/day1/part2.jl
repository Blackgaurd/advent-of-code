function main()
    io = open("day1/input.txt")

    snacks = [0]
    for line in eachline(io)
        if line == ""
            push!(snacks, 0)
            continue
        end
        snacks[end] += parse(Int, line)
    end

    sort!(snacks)
    top3 = snacks[end-2:end]
    println(sum(top3))

    close(io)
end

main()