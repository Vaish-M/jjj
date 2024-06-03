import React, { Component } from 'react';
import "./Details.css"
import { Navigate, useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPencil, faTrash} from '@fortawesome/free-solid-svg-icons';
import axios from 'axios';
import { data } from 'jquery';
class Details extends Component{
    constructor(props) {
        super(props);
        this.state = {
          data:[],
          currentPage: 1,
          itemsPerPage: 7,
          predict:'',
          id:'',
          formData:[],
          skill:[],
        };
      }

      showFileInput = () => {
        this.setState({ fileInputVisible: true });
      }

     
      handleFileUpload = (e) => {
        const file = e.target.files[0];
        if (file && file.type === 'text/csv') {
            const formData = new FormData();
            formData.append('file', file); 
    
            axios.post('http://127.0.0.1:5000/upload_students', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data', 
                },
            })
            .then((response) => {
                alert('Data uploaded successfully');
                window.location.reload();
            })
            .catch((error) => {
                console.error('Error uploading data:', error);
            });
        } else {
            alert('Please select a valid CSV file.');

        }
    }
    
      handleSubmit = (e)=> {
        e.preventDefault()
        
      }
      handlePageChange = (newPage) => {
        this.setState({ currentPage: newPage });
      };
      componentDidMount(){
        axios.get("http://127.0.0.1:5000/student_data")
            .then(response => {
                this.setState({ data: response.data });
                console.log(response.data)
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
      }


      handleSubmit = (e)=> {
        e.preventDefault()
        
      }
      handlePageChange = (newPage) => {
        this.setState({ currentPage: newPage });
      };

     
// handleEdit = (studentId, updatedDetails) => {
//   axios.post('http://127.0.0.1:5000/edit_student', {
//       id: studentId,
//       NAMES: updatedDetails.NAMES,
      
//   })
//   .then(response => {
//       alert('Student details updated successfully');
//       window.location.reload();
//   })
//   .catch(error => {
//       console.error('Error updating student details:', error);
//   });
// }

handleDelete = () => {
  const confirmed = window.confirm('Are you sure you want to delete this student?');

  if (confirmed) {
    axios
      .post('http://127.0.0.1:5000/delete_student', {
        id: this.state.id,
      })
      .then(response => {
        alert('Student deleted successfully');
        window.location.reload();
      })
      .catch(error => {
        console.error('Error deleting student:', error);
      });
  }
};

      componentDidMount(){
        axios.get("http://127.0.0.1:5000/student_data")
            .then(response => {
                this.setState({ data: response.data });
                console.log(response.data)
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
      }
     

      renderTable() {
        if (this.state.data.length === 0) {
            return <p>No data available.</p>;
        }
        const { data, currentPage, itemsPerPage } = this.state;
        const startIndex = (currentPage - 1) * itemsPerPage;
        const endIndex = startIndex + itemsPerPage;
        const currentData = data.slice(startIndex, endIndex);
        return (
        <div className='detail'>
            <div className='button'>
            <input type="file" name="file" accept=".csv" onChange={this.handleFileUpload} />
            </div>
            <div className='mydiv'  style={{ overflowY: 'scroll', maxHeight: '700px',scrollbarWidth: 'none', WebkitOverflowScrolling: 'touch', scrollbarColor:'transparent' }}>
            <table>
                <thead>
                    <tr>
                        <th>NAMES</th>
                        <th>ACADEMICS</th>
                        <th>MOCK INTERVIEW</th>
                        <th>PYTHON</th>
                        <th>JAVA</th>
                        <th>DBMS</th>
                        <th>COMPUTER NETWORKS</th>
                        <th>MACHINE LEARNING</th>
                        <th>APTITUDE SKILLS</th>
                        <th>FULL STACK DEVELOPMENT</th>
                        <th>COMMUNICATION SKILLS</th>
                        <th>INTERNSHIPS</th>
                        <th>NUMBER OF CERTIFICATIONS</th>
                        <th>CERTIFICATIONS DOMAIN</th>
                        <th>NUMBER OF PROJECTS</th>
                        <th>PROJECT DOMAIN</th>
                        <th>SKILLS</th>

                        <th>PREDICTION</th>
                        {/* <th>OPTIONS</th> */}
                        

                    </tr>
                </thead>
                <tbody>
                {currentData.length > 3 ? (
  currentData.map((student, index) => (
    <tr key={student.id}>
      <td>{student.NAMES}</td>
      <td>{student.ACADEMICS}</td>
      <td>{student["MOCK INTERVIEW"]}</td>
      <td>{student.PYTHON}</td>
      <td>{student.JAVA}</td>
      <td>{student.DBMS}</td>
      <td>{student["COMPUTER NETWORKS"]}</td>
      <td>{student["MACHINE LEARNING"]}</td>
      <td>{student["APTITUDE SKILLS"]}</td>
      <td>{student["FULL STACK DEVELOPMENT"]}</td>
      <td>{student["COMMUNICATION SKILLS"]}</td>
      <td>{student.INTERNSHIPS}</td>
      <td>{student["NUMBER OF CERTIFICATIONS"]}</td>
      <td>{student["CERTIFICATIONS DOMAIN"]}</td>
      <td>{student["NUMBER OF PROJECTS"]}</td>
      <td>{student["PROJECT DOMAIN"]}</td>
      <td>{student.SKILLS}</td>
      
      <td>
        <a href='#popup1'><button className='predict' onClick={() => this.setState({ predict:student.STATUS, skill: student.REMARKS })}>PREDICT</button></a>
      </td>
    {/* <td><button style={{color:'white',backgroundColor:'red',padding:'5px'}} onClick={() => {
    this.setState({ id: student.id }, () => {
        this.handleDelete();
    });
}}><FontAwesomeIcon icon={faTrash} /></button>
    <button style={{color:'white',backgroundColor:'green',padding:'5px',marginLeft:'10px'}} onClick={() => {
      
        this.setState({ formData: student }, () => {
          localStorage.setItem('formDate',JSON.stringify(student));
          this.props.navigate('/user/edit');
      });
       
    }}><FontAwesomeIcon icon={faPencil} /></button>
    </td> */}

      
    </tr>
  ))
) : (
  <tr>
    <td colSpan="18">No data available.</td>
  </tr>
)}

                </tbody>
            </table>
            <div className="pagination" style={{float:'left'}}>
                {currentPage > 1 && (
                    <button onClick={() => this.handlePageChange(currentPage - 1)}>Previous</button>
                )}
                {currentData.length === itemsPerPage && (
                    <button onClick={() => this.handlePageChange(currentPage + 1)}>Next</button>
                )}
            </div>
            </div>
        </div>
        );
    }
    handleAction(id) {
        console.log(`Button clicked for student ID ${id}`);
    }
    render(){
        
        return(
            <div>
                {this.renderTable()}
                <div id="popup1" className="overlay1">
      <div className="popup1">
         {/* eslint-disable-next-line */}
        <a className="close" href="#">&times;</a>
        
        <h2>{this.state.predict}</h2>
        <h2>{this.state.skill}</h2>
        </div>
        </div>
        </div>
        );
    }
}
export default Details;

export function ResultRouter(props){
    const navigate=useNavigate()
    return (<Details navigate={navigate}></Details>)
}