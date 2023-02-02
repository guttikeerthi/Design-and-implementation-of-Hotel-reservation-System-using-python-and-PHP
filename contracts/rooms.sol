// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract rooms {

  address[] _customers;
  string[] _aadhars;
  string[] _city;
  uint[] _noofrooms;
  uint[] _noofdays;
  string[] _dates;
  string[] _noofadults;
  uint[][] _roomids;

  uint totalrooms=10;
  uint[] status=[0,0,0,0,0,0,0,0,0,0]; 
  
  function roomrequest(address customer,string memory aadhar,string memory city,uint noofrooms,uint noofdays,string memory date,string memory noofadults) public{

    _customers.push(customer);
    _aadhars.push(aadhar);
    _city.push(city);
    _noofrooms.push(noofrooms);
    _noofdays.push(noofdays);
    _dates.push(date);
    _noofadults.push(noofadults);
    _roomids.push([0]);
  } 

  function viewrequests() public view returns(address[] memory,string[] memory,string[] memory,uint[] memory,uint[] memory,string[] memory,string[] memory,uint[][] memory){
    return(_customers,_aadhars,_city,_noofrooms,_noofdays,_dates,_noofadults,_roomids);
  }

  function allocateroom(address customer,uint[] memory id) public{
    uint i;
    uint j;

    for(i=0;i<_customers.length;i++){
      if(customer==_customers[i]){
        _roomids[i]=id;
      }
    }
    for(j=0;j<id.length;j++){
      status[id[j]-1]=1;  
    }
  }

  function viewroomstatus() public view returns(uint[] memory){
    return(status);
  }

  function vacateroom(address customer) public{
    uint i;
    uint j;
    uint[] memory id;

    for(i=0;i<_customers.length;i++){
      if(customer==_customers[i]){
          id=_roomids[i];
      }
    }
    for(j=0;j<id.length;j++){
      status[id[j]-1]=0;
    }
  }
}
