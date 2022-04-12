pragma solidity ^0.8.1;

contract SendMoneyExample {

    uint public balanceValue;
    
    function receiveMoney() public payable {
        balanceValue += msg.value;
    }

    function getBalance() public view returns(uint) {
        return address(this).balance;
    }

    function withdrawMoney() public {
        address to = msg.sender;
        payable(to).transfer(this.getBalance());
    }

    function withdrawMoneyTo(address _to) public {
        payable(_to).transfer(this.getBalance());
    }
}