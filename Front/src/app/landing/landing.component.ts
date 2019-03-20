import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { DepartmentDescriptionComponent } from '../department-description/department-description.component';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.scss']
})
export class LandingComponent implements OnInit {

  public left = 1;
  public isLast = false;

  private quantityOfSlides = 5;

  constructor(
    private modalService: NgbModal,
  ) { }

  public ngOnInit() {}

  public nextSlide(): void {
    this.isLast = false;
    if (this.left === this.quantityOfSlides) {
      this.left = this.left + 1;
      setTimeout(() => {
        this.isLast = true;
        this.left = 1;
      }, 500);
    }

    if (this.left < this.quantityOfSlides) {
      this.left = this.left + 1;
      console.log(this.left);
    }
  }

  public prevSlide(): void {
    this.isLast = false;
    if (this.left === 1) {
      this.left = this.left - 1;
      setTimeout(() => {
        this.isLast = true;
        this.left = this.quantityOfSlides;
      }, 500);
    }

    if (this.left > 1) {
      this.left = this.left - 1;
      console.log(this.left);
    }
  }

  public navigate(value: number): void {
    this.isLast = false;
    if (this.left > 0 || this.left < 6) {
      this.left = value;
    }
  }

  public openDescription(): void {
    console.log('sd');
    this.modalService.open(
      DepartmentDescriptionComponent,
      {
        centered: true,
        windowClass: 'dark-modal',
        backdrop: 'static'
      }
    );
  }

  private sliding(): void {
    setInterval(() => this.nextSlide(), 2000);
  }
}
