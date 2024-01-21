use strict;
use warnings;
use JSON;

package ConnectApril;

sub recv_request {
    my $n = $ARGV[$#ARGV];
    my $file_path = ".$n.input";

    eval {
        open my $file, '<', $file_path or die $!;
        local $/;
        my $data = <$file>;
        close $file;
        return JSON::decode_json($data);
    } or do {
        my $err = $@;
        warn $err;
        return;
    };
}

sub send_response {
    my ($response) = @_;
    my $n = $ARGV[$#ARGV];
    my $file_path = ".$n.output";

    eval {
        open my $file, '>', $file_path or die $!;
        print $file JSON::encode_json($response);
        close $file;
    } or do {
        my $err = $@;
        warn $err;
    };
}

1;