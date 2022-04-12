pragma solidity >=0.8.1;

contract StartStopUpdateExample {

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    function sendMoney() public payable {

    }

    function withdrawAllMoney(address  _to) public {
        require( _to ==  , "Empty Address");
        require( owner == msg.sender , "You can not send the money");
        payable(_to).transfer(address(this).balance); 
        
    }
}