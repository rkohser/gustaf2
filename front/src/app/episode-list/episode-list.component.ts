import { GustafDbService } from '../gustaf-db.service';
import { GustafStatusService } from '../gustaf-status.service';
import { Component, OnInit } from '@angular/core';
import { Episode } from '../episode';
import { Show } from '../show';

@Component({
  selector: 'app-episode-list',
  templateUrl: './episode-list.component.html',
  styleUrls: ['./episode-list.component.css']
})
export class EpisodeListComponent implements OnInit {

  episodes: Episode[];

  constructor(
    private gustafDbService: GustafDbService,
    private gustafStatusService: GustafStatusService
  ) {
    // Observe current show and update show list
    gustafStatusService.currentShow$.subscribe(
      show => this.getEpisodes(show)
    );
  }

  getEpisodes(show_id: string) {
    this.gustafDbService.getEpisodesPerShow(show_id)
      .then(episodes => this.episodes = episodes);
  }


  ngOnInit() {
    this.getEpisodes('Ballers');
  }

}
