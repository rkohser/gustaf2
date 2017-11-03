import { GustafDbService } from '../gustaf-db.service';
import { Show } from '../show';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-show-list',
  templateUrl: './show-list.component.html',
  styleUrls: ['./show-list.component.css']
})
export class ShowListComponent implements OnInit {

  shows: Show[];

  public showsForm: FormGroup;

  constructor(
    private gustafDbService: GustafDbService,
    private formBuilder: FormBuilder
  ) { }

  getShows(): void {
    this.gustafDbService
      .getShows()
      .then(shows => this.shows = shows);
  }

  ngOnInit() {
    this.getShows();
    this.showsForm = this.formBuilder.group({
      'model': null
    });
  }

}
