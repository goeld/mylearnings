// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.1;

contract WorkingWithVariables {
    uint256 public myUint;

    function setMyUnit(uint _myUint) public {
        myUint = _myUint;
    }

    bool public myBool;

    function setMyBool(bool _myBool) public {
        myBool = _myBool;
    }

    uint8 public myUint8;

    function setMyUint8(uint8 _myUint8) public {
        myUint8 = _myUint8;
    }

    function incrementMyUint() public {
        myUint8++;
    }

    function decrementMyUint8() public {
        myUint8--;
    }

    address public myAddress;

    function setMyAddress(address _myAddress) public {
        myAddress = _myAddress;
    }

    function getBalanceOfMyAddress() public view returns(uint) {
        return myAddress.balance;
    }

    function getBalanceByAddress(address _address) public view returns(uint) {
        return _address.balance;
    }

    string public myString;

    function setMyString(string memory _myString) public {
        myString = _myString;
    }
}