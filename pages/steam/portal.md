---
title: "Portal"
description: "Steam achievements and progress for Portal - 26.67% complete with 4/15 achievements unlocked."
date: "2022-06-02"
templateKey: steam_game
steam:
  game: "Portal"
  app_id: 400
  total_achievements: 15
  unlocked_achievements: 4
  completion_percentage: 26.67
  playtime_hours: 19.7
  last_played: "2022-06-02"
  description: ""
  developers: []
  publishers: []
tags: ["steam", "game", "portal"]
url: "/portal/"
slug: "steam/portal"
---

<style>
.game-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 30px;
  margin: 30px 0;
  padding: 20px;
  background: #1a1a1a;
  border-radius: 12px;
  border: 1px solid #333;
}

.game-header img {
  width: 200px;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  border: 1px solid #333;
  flex-shrink: 0;
}

.game-info {
  flex: 1;
}

.game-info h1 {
  margin: 0 0 15px 0;
  color: #fff;
  font-size: 2em;
}

.game-info p {
  margin: 0 0 15px 0;
  color: #ccc;
  line-height: 1.5;
}

.game-info .developers {
  font-size: 0.9em;
  color: #999;
}

.game-links {
  margin-top: 20px;
}

.game-links a {
  display: inline-block;
  margin-right: 15px;
  padding: 8px 12px;
  background: #2a2a2a;
  color: #fff;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9em;
  transition: background-color 0.2s ease;
}

.game-links a:hover {
  background: #3a3a3a;
  color: #4caf50;
}

.steam-game-progress {
  background: #1a1a1a;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid #333;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin: 20px 0;
}

.stat-card {
  background: #2a2a2a;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  border: 1px solid #444;
}

.stat-card h3 {
  margin: 0 0 15px 0;
  color: #4caf50;
  font-size: 1.1em;
}

.stat-value {
  font-size: 2em;
  font-weight: bold;
  color: #fff;
  margin: 10px 0;
}

.stat-card p {
  margin: 10px 0 0 0;
  color: #ccc;
  font-size: 0.9em;
}

.progress-bar {
  width: 100%;
  height: 24px;
  background: #2a2a2a;
  border-radius: 12px;
  overflow: hidden;
  margin: 10px 0;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4caf50, #8bc34a);
  border-radius: 12px;
  transition: width 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-weight: bold;
  font-size: 12px;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(125px, 1fr));
  gap: 8px;
  margin: 20px 0;
}

.achievement-item {
  position: relative;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.achievement-item:hover {
  transform: scale(1.1);
  z-index: 10;
}

.achievement-icon-wrapper {
}

.achievement-icon {
    margin:0;
    padding:0;
  border-radius: 6px;
  border: 2px solid #444;
  transition: border-color 0.2s ease;
}

.achievement-item.unlocked .achievement-icon {
  border-color: #4caf50;
  box-shadow: 0 0 10px rgba(76, 175, 80, 0.3);
}

.achievement-item.locked .achievement-icon {
  filter: grayscale(100%);
  opacity: 0.6;
}

.achievement-tooltip {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0, 0, 0, 0.95);
  color: white;
  padding: 8px 12px;
  border-radius: 6px;
  font-size: 12px;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  z-index: 100;
  margin-bottom: 5px;
  max-width: 200px;
  white-space: normal;
  text-align: center;
}

.achievement-item:hover .achievement-tooltip {
  opacity: 1;
}

.achievement-section {
  background: #1a1a1a;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
  border: 1px solid #333;
}

.achievement-section h2 {
  margin-top: 0;
  color: #fff;
}
</style>

<div class="game-header">
  <img src="https://cdn.akamai.steamstatic.com/steam/apps/400/library_600x900.jpg" alt="Portal box art" loading="lazy" 
       onerror="this.src='https://cdn.akamai.steamstatic.com/steam/apps/400/header.jpg'">
  <div class="game-info">
    <h1>Portal</h1>
    
    

  </div>
</div>

<div class="steam-game-progress">
<h2>🎮 Game Progress & Stats</h2>

<div class="stats-grid">
  <div class="stat-card">
    <h3>Achievements</h3>
    <div class="progress-bar">
      <div class="progress-fill" style="width: 26.67%">
        26.67%
      </div>
    </div>
    <p>4/15 Unlocked</p>
  </div>
  
  <div class="stat-card">
    <h3>Playtime</h3>
    <div class="stat-value">19.7h</div>
    <p>Total hours played</p>
  </div>
  
  <div class="stat-card">
    <h3>Last Played</h3>
    <div class="stat-value">2022-06-02</div>
    <p>Most recent session</p>
  </div>
</div>
</div>


<div class="achievement-section">
<h2>🏆 Unlocked Achievements (4)</h2>

<div class="achievements-grid">

<div class="achievement-item unlocked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_getportalguns.jpg" alt="Lab Rat" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Lab Rat</strong><br>
    Acquire the fully powered Aperture Science Handheld Portal Device.<br>
    <small>Unlocked: March 16, 2022</small>
  </div>
</div>
<div class="achievement-item unlocked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_kill_companioncube.jpg" alt="Fratricide" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Fratricide</strong><br>
    Do whatever it takes to survive.<br>
    <small>Unlocked: March 26, 2022</small>
  </div>
</div>
<div class="achievement-item unlocked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_escape_testchambers.jpg" alt="Partygoer" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Partygoer</strong><br>
    Make the correct party escort submission position decision.<br>
    <small>Unlocked: May 31, 2022</small>
  </div>
</div>
<div class="achievement-item unlocked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_hit_turret_with_turret.jpg" alt="Friendly Fire" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Friendly Fire</strong><br>
    Knock down a turret with another turret.<br>
    <small>Unlocked: March 26, 2022</small>
  </div>
</div>
</div>
</div>

<div class="achievement-section">
<h2>🔒 Locked Achievements (11)</h2>

<div class="achievements-grid">

<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_beat_game_bw.jpg" alt="Heartbreaker" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Heartbreaker</strong><br>
    Complete Portal.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_infinitefall_bw.jpg" alt="Terminal Velocity" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Terminal Velocity</strong><br>
    Fall 30,000 feet.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_longjump_bw.jpg" alt="Long Jump" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Long Jump</strong><br>
    Jump 300 feet.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_beat_2advancedmaps_bw.jpg" alt="Cupcake" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Cupcake</strong><br>
    Beat two Portal advanced maps.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_beat_4advancedmaps_bw.jpg" alt="Fruitcake" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Fruitcake</strong><br>
    Beat four Portal advanced maps.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_beat_6advancedmaps_bw.jpg" alt="Vanilla Crazy Cake" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Vanilla Crazy Cake</strong><br>
    Beat all six Portal advanced maps.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_get_allbronze_bw.jpg" alt="Basic Science" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Basic Science</strong><br>
    Earn bronze medals on all Portal challenges.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_get_allsilver_bw.jpg" alt="Rocket Science" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Rocket Science</strong><br>
    Earn silver medals on all Portal challenges.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_get_allgold_bw.jpg" alt="Aperture Science" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Aperture Science</strong><br>
    Earn gold medals on all Portal challenges.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/portal_detach_all_cameras_bw.jpg" alt="Camera Shy" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Camera Shy</strong><br>
    Detach security cameras from the walls.
  </div>
</div>
<div class="achievement-item locked">
  <span class="achievement-icon-wrapper">
    <img src="https://steamcdn-a.akamaihd.net/steamcommunity/public/images/apps/400/d3a7fbca2549d043955d33cb5eaf30259dcf41ac.jpg" alt="Transmission Received" class="achievement-icon">
  </span>
  <div class="achievement-tooltip">
    <strong>Transmission Received</strong><br>
    ..?
  </div>
</div>
</div>
</div>

---

*Game data automatically imported from Steam. Achievement links will be created as individual posts when achievements are unlocked.*
