
<?php  

    if(isset ($_GET['submit']))
        
            {
            $n1=$_GET['uname'];
            $n2=$_GET['pass'];
        
            if($n1=="subodh.meshram4@gmail.com" && $n2=="subodh")
                echo "welcom subodh";
            else
                echo "invalid user";
            }
            ?>
    