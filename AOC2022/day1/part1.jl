function main()
    io = open("day1/input.txt")

    mx = 0
    cur = 0
    for line in eachline(io)
        if line == ""
            cur = 0
            continue
        end
        cur += parse(Int, line)
        mx = max(mx, cur)
    end

    println(mx)

    close(io)
end

main()