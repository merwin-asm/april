open System.IO
open Newtonsoft.Json

type ConnectApril() =
    static member recvRequest() =
        let n = int (System.Environment.GetCommandLineArgs().[System.Environment.GetCommandLineArgs().Length - 1])
        let filePath = sprintf ".%d.input" n

        try
            let data = File.ReadAllText(filePath)
            JsonConvert.DeserializeObject(data)
        with
        | ex -> 
            Console.Error.WriteLine(ex.Message)
            null

    static member sendResponse response =
        let n = int (System.Environment.GetCommandLineArgs().[System.Environment.GetCommandLineArgs().Length - 1])
        let filePath = sprintf ".%d.output" n

        try
            File.WriteAllText(filePath, JsonConvert.SerializeObject(response))
        with
        | ex -> Console.Error.WriteLine(ex.Message)