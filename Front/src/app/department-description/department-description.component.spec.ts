import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DepartmentDescriptionComponent } from './department-description.component';

describe('DepartmentDescriptionComponent', () => {
  let component: DepartmentDescriptionComponent;
  let fixture: ComponentFixture<DepartmentDescriptionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DepartmentDescriptionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DepartmentDescriptionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
