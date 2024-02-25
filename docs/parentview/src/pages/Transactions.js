import React from "react";
import { useState } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCheck, faCog, faHome, faSearch } from '@fortawesome/free-solid-svg-icons';
import { Col, Row, Form, Button, ButtonGroup, Breadcrumb, InputGroup, Dropdown } from '@themesberg/react-bootstrap';

import Profile3 from "../assets/img/team/profile-picture-3.jpg";
import { TransactionsTable } from "../components/Tables";


// Include all parent children in dashboard
const ProfileSelector = ({ profiles }) => {
  const [selectedProfle,  setselectedProfile] = useState(null);


  return (
    <div className="d-flex flex-wrap justify-content-start">
      {profiles.map(profile => (
        <div key={profile.id} className="m-2">
          <Button className="{ `btn btn-outline-primary rounded-circle ${selectedProfile === profile.id && 'border border-primary'}` }">
            <img src="{ profile.path }" alt={ profile.id } className="img-fluid rounded-circle"  style={{ width: "200px", height:'200px' }}></img>
          </Button>
        </div>
        ))}
    </div>
    )
}





export default () => {


  const profiles = [
    {path: 'Iyanu.jpg', id: 1},
    {path: Profile3, id: 2}
  ]

  return (
    <>
      <div className="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center py-4">
        <div className="d-block mb-4 mb-md-0">
          <Breadcrumb className="d-none d-md-inline-block" listProps={{ className: "breadcrumb-dark breadcrumb-transparent" }}>
            <Breadcrumb.Item><FontAwesomeIcon icon={faHome} /></Breadcrumb.Item>
            <Breadcrumb.Item>Parent Dashboard</Breadcrumb.Item>
            <Breadcrumb.Item active>Student's Performance</Breadcrumb.Item>
          </Breadcrumb>
          <h4>FirstName Performance</h4>
          <p className="mb-0">Current Session: 2023/2024</p>
          <p className="mb-0">Current Term: First Term</p>
        </div>
        <div className="btn-toolbar mb-2 mb-md-0">
          <ButtonGroup>
            <Button variant="outline-primary" size="sm">Share</Button>
            <Button variant="outline-primary" size="sm">Export</Button>
          </ButtonGroup>
        </div>
      </div>

      {/* <ProfileSelector profiles={profiles}/> */}

      <div className="table-settings mb-4">
        <Row className="justify-content-between align-items-center">
          <Col xs={8} md={6} lg={3} xl={4}>
            <ProfileSelector profiles={profiles}/>
          </Col>
          <Col xs={4} md={2} xl={1} className="ps-md-0 text-end">
            <Dropdown as={ButtonGroup}>
              <Dropdown.Toggle split as={Button} variant="link" className="text-dark m-0 p-0">
                <span className="icon icon-sm icon-gray">
                  <FontAwesomeIcon icon={faCog} />
                </span>
              </Dropdown.Toggle>
              <Dropdown.Menu className="dropdown-menu-xs dropdown-menu-right">
                <Dropdown.Item className="fw-bold text-dark">Show</Dropdown.Item>
                <Dropdown.Item className="d-flex fw-bold">
                  10 <span className="icon icon-small ms-auto"><FontAwesomeIcon icon={faCheck} /></span>
                </Dropdown.Item>
                <Dropdown.Item className="fw-bold">20</Dropdown.Item>
                <Dropdown.Item className="fw-bold">30</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
          </Col>
        </Row>
      </div>

      <TransactionsTable />
    </>
  );
};
