var NewSimpleStorage = artifacts.require("NewSimpleStorage");

module.exports = function(deployer) {
  // Pass 42 as first param to contract

  deployer.deploy (SimpleStorage, 42, {privateFor: [""]  })


};
