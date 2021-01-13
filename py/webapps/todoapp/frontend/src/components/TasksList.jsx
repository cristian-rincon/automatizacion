import React from "react";
import { Icon } from "react-icons-kit";
import { ic_create, ic_delete } from "react-icons-kit/md";

class TasksList extends React.Component {

  render() {
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
  }
}

export default TasksList;
