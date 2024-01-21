-module(connect_april).
-export([recv_request/0, send_response/1]).

recv_request() ->
    {ok, [N | _]} = io:format("~s", [hd(lists:reverse(code:root_dir()))]),
    N_str = list_to_integer(N),
    FilePath = lists:concat([".", integer_to_list(N_str), ".input"]),
    case file:read_file(FilePath) of
        {ok, Data} ->
            {ok, json:decode(Data)};
        {error, Reason} ->
            io:format("Error: ~p~n", [Reason]),
            null
    end.

send_response(Response) ->
    {ok, [N | _]} = io:format("~s", [hd(lists:reverse(code:root_dir()))]),
    N_str = list_to_integer(N),
    FilePath = lists:concat([".", integer_to_list(N_str), ".output"]),
    case file:write_file(FilePath, json:encode(Response)) of
        ok ->
            ok;
        {error, Reason} ->
            io:format("Error: ~p~n", [Reason])
    end.