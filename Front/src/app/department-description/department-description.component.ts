import { Component } from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-department-description',
  templateUrl: './department-description.component.html',
  styleUrls: ['./department-description.component.scss']
})
export class DepartmentDescriptionComponent {

  constructor(
    private modal: NgbActiveModal
  ) { }

  public close(): void {
    this.modal.close();
  }
}
