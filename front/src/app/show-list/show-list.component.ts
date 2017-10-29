import { GustafDbService } from '../gustaf-db.service';
import { Show } from '../show';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-show-list',
  templateUrl: './show-list.component.html',
  styleUrls: ['./show-list.component.css']
})
export class ShowListComponent implements OnInit {

  shows: Show[];

  constructor(
    private gustafDbService: GustafDbService
  ) { }

  getShows(): void {
    this.gustafDbService
      .getShows()
      .then(shows => this.shows = shows);
  }

  ngOnInit() {
    this.getShows();
  }

}
