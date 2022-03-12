pragma solidity >=0.4.22 <0.9.0;

contract SimpleStorage {
 uint public storedData;
 constructor(uint initVal) public {
  storedData = initVal;
 }

 function set(uint x) public {

  storedData = x; 
 }

 function get() view public returns (uint retVal) {
  return storedData;
 }







}
