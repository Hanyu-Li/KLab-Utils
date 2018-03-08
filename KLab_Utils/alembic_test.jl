using Alembic
using ArgParse
function parse_commandline()
    s = ArgParseSettings()
    @add_arg_table s begin
        "--opt1"
            help = "an option with an argument"
        "--opt2", "-o"
            help = "another option with an argument"
            arg_type = Int
            default = 0
        "--flag1"
            help = "an option without argument, i.e. a flag"
            action = :store_true
        "--config"
            help = "a positional argument"
            required = false
            default = "/mnt/md0/KLab_Util_test/Alembic_test/local_params/test.json"
            
    end

    return parse_args(s)
end

function main()
    parsed_args = parse_commandline()
    println("Parsed args:")
    for (arg,val) in parsed_args
        println("  $arg  =>  $val")
    end
    params = parsed_args["config"]
    println(params)
    load_params(params)
    ms = make_stack(); # make meshset given the params specified in the JSON file
    match!(ms); # blockmatch between the meshes in the meshset, per the params
    elastic_solve!(ms); # relax the spring system
    render(ms); # render the images and save to CloudVolume

end

main()