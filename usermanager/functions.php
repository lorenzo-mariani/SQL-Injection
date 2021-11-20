<?php

function _dbgWrite($msg) {
    $DebugOn = 1;//$container->get('settings')['DebugModeEnabled'];
    if ($DebugOn == 1)
    {
        $file = 'debug.log';
        $current = file_get_contents($file);
        $current .= $msg."\n";
        file_put_contents($file, $current);
    }
}


        function connectDB(){
            $serverName = "localhost";
            //$connectionInfo = array( "Database"=>"EDI", "UID"=>"sa", "PWD"=>"eD1project");
            $connectionInfo = array( "Database"=>"edi", "UID"=>"root", "PWD"=>"eD1project");
            $conn = mysqli_connect($serverName, $connectionInfo['UID'], $connectionInfo['PWD'],  $connectionInfo['Database']);
            return $conn;
        }


    function getUsers($comp_name) {

        $conn = connectDB();
        $query = "SELECT * FROM users WHERE comp_name = '".$comp_name."'";

        $stmt = mysqli_query( $conn, $query);

        if( $stmt === false ) {
            die( print_r(  mysqli_errors(), true));
        }
        $row =  mysqli_fetch_array( $stmt, MYSQLI_ASSOC);
        if(!empty($row))
        {
            $stmt = mysqli_query( $conn, $query);

            while(!empty($row = mysqli_fetch_array( $stmt, MYSQLI_ASSOC))){
                $users[] = $row;
            }

        }else{
            return false;
        }

        return $users;

    }


function getAziende($idaz) {

    $json = json_encode(array('idaz' => $idaz));
    $curl = curl_init();

    curl_setopt_array($curl, array(
        CURLOPT_RETURNTRANSFER => 1,
        CURLOPT_URL => 'http://www.progettoweb.it/ws/public/index.php/getAziende',
        CURLOPT_USERAGENT => 'Codular Sample cURL Request',
    ));
    curl_setopt( $curl, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($curl, CURLOPT_POSTFIELDS, $json);
    curl_setopt($curl, CURLOPT_HTTPHEADER, array(
            'Content-Type:application/json;charset=UTF-8',
            'Content-Length: ' . strlen($json))
    );

    curl_setopt($curl, CURLOPT_POST, true);
    $resp = curl_exec($curl);
    curl_close($curl);


    if ($resp == false)	{
        _dbgWrite("failed_getAziende");
        return false;
    }

    return json_decode($resp);
}
?>
