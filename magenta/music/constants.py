# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Constants for music processing in Magenta."""

# Meter-related constants.
DEFAULT_QUARTERS_PER_MINUTE = 120.0
DEFAULT_STEPS_PER_BAR = 16  # 4/4 music sampled at 4 steps per quarter note.
DEFAULT_STEPS_PER_QUARTER = 4

# Default absolute quantization.
DEFAULT_STEPS_PER_SECOND = 100

# Standard pulses per quarter.
# https://en.wikipedia.org/wiki/Pulses_per_quarter_note
STANDARD_PPQ = 220

# Special melody events.
NUM_SPECIAL_MELODY_EVENTS = 2
MELODY_NOTE_OFF = -1
MELODY_NO_EVENT = -2

# Other melody-related constants.
MIN_MELODY_EVENT = -2
MAX_MELODY_EVENT = 127
MIN_MIDI_PITCH = 0  # Inclusive.
MAX_MIDI_PITCH = 127  # Inclusive.
NOTES_PER_OCTAVE = 12

# Velocity-related constants.
MIN_MIDI_VELOCITY = 1  # Inclusive.
MAX_MIDI_VELOCITY = 127  # Inclusive.

# Program-related constants.
MIN_MIDI_PROGRAM = 0
MAX_MIDI_PROGRAM = 127

# Chord symbol for "no chord".
NO_CHORD = 'N.C.'

# The indices of the pitch classes in a major scale.
MAJOR_SCALE = [0, 2, 4, 5, 7, 9, 11]

# NOTE_KEYS[note] = The major keys that note belongs to.
# ex. NOTE_KEYS[0] lists all the major keys that contain the note C,
# which are:
# [0, 1, 3, 5, 7, 8, 10]
# [C, C#, D#, F, G, G#, A#]
#
# 0 = C
# 1 = C#
# 2 = D
# 3 = D#
# 4 = E
# 5 = F
# 6 = F#
# 7 = G
# 8 = G#
# 9 = A
# 10 = A#
# 11 = B
#
# NOTE_KEYS can be generated using the code below, but is explicitly declared
# for readability:
# NOTE_KEYS = [[j for j in range(12) if (i - j) % 12 in MAJOR_SCALE]
#              for i in range(12)]
NOTE_KEYS = [
    [0, 1, 3, 5, 7, 8, 10],
    [1, 2, 4, 6, 8, 9, 11],
    [0, 2, 3, 5, 7, 9, 10],
    [1, 3, 4, 6, 8, 10, 11],
    [0, 2, 4, 5, 7, 9, 11],
    [0, 1, 3, 5, 6, 8, 10],
    [1, 2, 4, 6, 7, 9, 11],
    [0, 2, 3, 5, 7, 8, 10],
    [1, 3, 4, 6, 8, 9, 11],
    [0, 2, 4, 5, 7, 9, 10],
    [1, 3, 5, 6, 8, 10, 11],
    [0, 2, 4, 6, 7, 9, 11]
]

# For control signals:

# Complete set of composers in Yamaha2750
COMPOSER_SET = ['Agosti', 'Albeniz', 'Babajanian', 'Bach', 'Balakirev', 'Barber', 'Bartholdy', 'Bartok', 'Beethoven', 'Berg', 'Berio', 'Bizet', 'Bowen', 'Brahms', 'Busoni', 'Carter', 'Chopin', 'Clementi', 'Corigliano', 'Coulthard', 'Crumb', 'Cziffra', 'Danielpour', 'Debussy', 'Dutilleux', 'Enescu', 'Eotvos', 'Falla', 'Franck', 'Gao', 'Gershwin', 'Gibbons', 'Ginastera', 'Glinka', 'Godowsky', 'Gounod', 'Grainger', 'Granados', 'Grieg', 'Grunfeld', 'Gubaidulina', 'Hamelin', 'Handel', 'Haydn', 'Hess', 'Hindemith', 'Hirtz', 'Horowitz', 'Jalbert', 'Janacek', 'Kapustin', 'Kreisler', 'Kurtag', 'Kuzmenko', 'Leschetizky', 'Liebermann', 'Ligeti', 'Liszt', 'Louie', 'Lutoslawski', 'Martin', 'McIntyre', 'Medtner', 'Mendelssohn', 'Menotti', 'Messiaen', 'Morel', 'Moszkowski', 'Mozart', 'Mozetich', 'Muczynski', 'Mussorgsky', 'Myaskovsky', 'Nancarrow', 'Pachelbel', 'Paganini', 'Petri', 'Pletnev', 'Poulenc', 'Prokofiev', 'Purcell', 'Rachmaninoff', 'Rameau', 'Ravel', 'Rimsky-Korsakov', 'Rodrigo', 'Rzewski', 'Saint-Saens', 'Scarlatti', 'Schedrin', 'Schnittke', 'Schonberg', 'Schostakovich', 'Schubert', 'Schumann', 'Scriabin', 'Sheng', 'Shostakovich', 'Slonimsky', 'Soler', 'Strauss', 'Stravinsky', 'Szymanowski', 'Takemitsu', 'Taneyev', 'Tchaikovsky', 'Tchaikowsky', 'Verdi', 'Vine', 'Volodos', 'Wagner', 'Weber', 'Yang', 'Zaimont']

# Composer clusters
COMPOSER_CLUSTER_1 = [
'Chopin',
'Liszt',
'Schubert',
'Schumann',
'Brahms',
'Tchaikovsky',
'Mendelssohn',
'Paganini',
'Busoni',
'Moszkowski',
'Bizet',
'Bartholdy',
'Balakirev',
'Tchaikowsky',
'Strauss',
'Grieg',
'Horowitz',
'Wagner',
'Saint-Saens']

COMPOSER_CLUSTER_2 = ['Beethoven']

COMPOSER_CLUSTER_3 = [
'Bach', 
'Handel', 
'Purcell']

COMPOSER_CLUSTER_4 = [
'Prokofiev',
'Stravinsky',
'Bartok',
'Barber',
'Shostakovich',
'Ligeti',
'Myaskovsky',
'Schnittke',
'Hindemith',
'Mussorgsky',
'Schostakovich',
'Messiaen',
'Schonberg']

COMPOSER_CLUSTER_5 = [
'Ravel',
'Debussy']

COMPOSER_CLUSTER_6 = [
'Haydn',
'Mozart',
'Scarlatti',
'Clementi',
'Pachelbel']

COMPOSER_CLUSTER_7 = [
'Rachmaninoff', 
'Scriabin']

COMPOSER_CLUSTER_8 = [
'Kapustin',
'Gershwin']

# Create a list of composer clusters
COMPOSER_CLUSTERS = [COMPOSER_CLUSTER_1, COMPOSER_CLUSTER_2, COMPOSER_CLUSTER_3, COMPOSER_CLUSTER_4, COMPOSER_CLUSTER_5, COMPOSER_CLUSTER_6, COMPOSER_CLUSTER_7, COMPOSER_CLUSTER_8, COMPOSER_SET]