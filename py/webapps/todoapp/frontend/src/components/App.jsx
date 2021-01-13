import React, { Component } from "react";
import { Badge, Button, Card, CardHeader, CardBody, CardFooter } from "reactstrap";
import axios from "axios";

import { Icon } from "react-icons-kit";
import { ic_create, ic_delete, ic_add } from "react-icons-kit/md";

import Modal from "./Modal";
import "../App.css";
// import todoItems from "./mock/tasks";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {
        title: "",
        description: "",
        completed: false,
      },
      todoList: [],
    };
  }
  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get("http://localhost:8000/api/tasks/")
      .then((res) => this.setState({ todoList: res.data }))
      .catch((err) => console.log(err));
  };
  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };
  renderTabList = () => {
    return (
      <div className="tab-list">
        <Badge
          onClick={() => this.displayCompleted(true)}
          className={this.state.viewCompleted ? "active" : ""}
        >
          Complete
        </Badge>

        <Badge
          onClick={() => this.displayCompleted(false)}
          className={this.state.viewCompleted ? "" : "active"}
        >
          Incomplete
        </Badge>
      </div>
    );
  };
  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      (item) => item.completed === viewCompleted
    );
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center my-2"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo text-muted" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            onClick={() => this.editItem(item)}
            className="btn btn-secondary mr-2 rounded-circle"
          >
            <Icon icon={ic_create} size={24} />
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger rounded-circle"
          >
            <Icon icon={ic_delete} size={24} />
          </button>
        </span>
      </li>
    ));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = (item) => {
    this.toggle();
    if (item.id) {
      axios
        .put(`http://localhost:8000/api/task/${item.id}`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/tasks/", item)
      .then((res) => this.refreshList());
  };
  handleDelete = (item) => {
    axios
      .delete(`http://localhost:8000/api/task/${item.id}`)
      .then((res) => this.refreshList());
  };
  createItem = () => {
    const item = { title: "", description: "", completed: false };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  render() {
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <Card color="light">

            <CardHeader>
              {this.renderTabList()}
            </CardHeader>
            <CardBody>
              <ul className="list-group">
                {this.renderItems()}
              </ul>
            </CardBody>
              
              <CardFooter className="text-center">
                <Button
                  onClick={this.createItem}
                  color="success"
                  className="rounded-circle button__add"
                >
                  
                  <Icon icon={ic_add} size={30} />
                  
                </Button>

              </CardFooter>
            </Card>
              
            
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;
