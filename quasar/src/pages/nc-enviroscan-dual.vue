<template>
  <q-layout view="lhr lpr lfr">
    <!-- q-layout view="hhh lpl fff" -->
    <q-page-container>
      <q-header elevated class="bg-teal">
        <div class="row no-wrap shadow-1">
        <!-- // Map One Toolbar and Menu -->
        <q-toolbar class="col-4">
          <q-btn flat round dense icon="menu" class="q-mr-sm text-black">
            <q-tooltip>Map One Menu</q-tooltip>
            <q-menu content-class="bg-teal-1">
              <q-list dense style="min-width: 100px">
                <q-item clickable>
                  <q-item-section>Base Layers</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item tag="label" v-ripple>
                        <q-item-section avatar>
                          <q-radio v-on:input="showBaseLayer1" val="osm" v-model="baselayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>OpenStreetMap</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item tag="label" v-ripple>
                        <q-item-section avatar>
                          <q-radio v-on:input="showBaseLayer1" val="mapbox" v-model="baselayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>MapBox Satellite</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>

                <q-separator></q-separator>
                <q-item clickable>
                  <q-item-section>NC Well Data Layers, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arsenic (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Arsenic</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_arsenic_prcast" v-model="currentlayer1" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu1"></span></td>
                                      <td>&gt; 6.83</td>
                                      <td>&gt; 8.95</td>
                                      <td>&gt; 16.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu2"></span></td>
                                      <td>&ge; 6.83 &amp; &lt; 10.12</td>
                                      <td>&ge; 8.95 &amp; &lt; 14.93</td>
                                      <td>&ge; 16.0 &amp; &lt; 32.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu3"></span></td>
                                      <td>&ge; 10.12 &amp; &lt; 13.42</td>
                                      <td>&ge; 14.93 &amp; &lt; 20.92</td>
                                      <td>&ge; 32.0 &amp; &lt; 48.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu4"></span></td>
                                      <td>&ge; 13.42 &amp; &lt; 16.71</td>
                                      <td>&ge; 20.92 &amp; &lt; 26.9</td>
                                      <td>&ge; 48.0 &amp; &lt; 64.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu5"></span></td>
                                      <td>&ge; 16.71</td>
                                      <td>&ge; 26.9</td>
                                      <td>&ge; 64.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Cadmium (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Cadmium</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_cadmium_mean" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_cadmium_prcast" v-model="currentlayer1" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu1"></span></td>
                                      <td>&gt; 0.74</td>
                                      <td>&gt; 2.71</td>
                                      <td>&gt; 4.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu2"></span></td>
                                      <td>&ge; 0.74 &amp; &lt; 0.77</td>
                                      <td>&ge; 2.71 &amp; &lt; 4.72</td>
                                      <td>&ge; 4.0 &amp; &lt; 8.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu3"></span></td>
                                      <td>&ge; 0.77 &amp; &lt; 0.79</td>
                                      <td>&ge; 4.72 &amp; &lt; 6.72</td>
                                      <td>&ge; 8.0 &amp; &lt; 12.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu4"></span></td>
                                      <td>&ge; 0.79 &amp; &lt; 0.82</td>
                                      <td>&ge; 6.72 &amp; &lt; 8.73</td>
                                      <td>&ge; 12.0 &amp; &lt; 16.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu5"></span></td>
                                      <td>&ge; 0.82</td>
                                      <td>&ge; 8.73</td>
                                      <td>&ge; 16.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Lead (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Lead</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_lead_med" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_lead_mean" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_lead_prcast" v-model="currentlayer1" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu1"></span></td>
                                      <td>&gt; 11.69</td>
                                      <td>&gt; 39.22</td>
                                      <td>&gt; 20.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu2"></span></td>
                                      <td>&ge; 11.69 &amp; &lt; 19.83</td>
                                      <td>&ge; 39.22 &amp; &lt; 75.53</td>
                                      <td>&ge; 20.0 &amp; &lt; 40.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu3"></span></td>
                                      <td>&ge; 19.83 &amp; &lt; 27.98</td>
                                      <td>&ge; 75.53 &amp; &lt; 111.83</td>
                                      <td>&ge; 40.0 &amp; &lt; 60.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu4"></span></td>
                                      <td>&ge; 27.98 &amp; &lt; 36.12</td>
                                      <td>&ge; 111.83 &amp; &lt; 148.14</td>
                                      <td>&ge; 60.0 &amp; &lt; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu5"></span></td>
                                      <td>&ge; 36.12</td>
                                      <td>&ge; 148.14</td>
                                      <td>&ge; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqufill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item dense ag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Maganese (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Manganese</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_mng_med" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_mng_mean" v-model="currentlayer1" color="teal" /></td>
                            <td><q-radio v-on:input="showMap1PanelRadioLayer" val="ncwellwise_mng_prcast" v-model="currentlayer1" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu1"></span></td>
                                      <td>&gt; 184.4</td>
                                      <td>&gt; 213.09</td>
                                      <td>&gt; 20.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu2"></span></td>
                                      <td>&ge; 184.4 &amp; &lt; 350.8</td>
                                      <td>&ge; 213.09 &amp; &lt; 404.97</td>
                                      <td>&ge; 20.0 &amp; &lt; 40.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu3"></span></td>
                                      <td>&ge; 350.8 &amp; &lt; 517.2</td>
                                      <td>&ge; 404.97 &amp; &lt; 596.85</td>
                                      <td>&ge; 40.0 &amp; &lt; 60.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu4"></span></td>
                                      <td>&ge; 517.2 &amp; &lt; 683.6</td>
                                      <td>&ge; 596.85 &amp; &lt; 788.73</td>
                                      <td>&ge; 60.0 &amp; &lt; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu5"></span></td>
                                      <td>&ge; 683.6</td>
                                      <td>&ge; 788.73</td>
                                      <td>&ge; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Socioeconomic Layers, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <tr>
                                  <td style="padding:5px"><span class="acssqu1"></span></td>
                                  <td>&gt; 15%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu2"></span></td>
                                  <td>&ge; 15% &amp; &lt; 30%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu3"></span></td>
                                  <td>&ge; 30% &amp; &lt; 45%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu4"></span></td>
                                  <td>&ge; 45% &amp; &lt; 60%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu5"></span></td>
                                  <td>&ge; 60% &amp; &lt; 75%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu6"></span></td>
                                  <td>&ge; 75%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="squfill"></span></td>
                                  <td>Fill -999.99</td>
                                </tr>
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="percent_below_poverty_level" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Below the Poverty Level</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="american_indian_and_alaska_native_alone" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Native American</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="asian_alone" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Asian</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="black_or_african_american_alone" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic Black</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="native_hawaiian_and_other_pacific_islander_alone" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic Native Hawaiian and other Pacific Islander</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="white_alone" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic White</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="two_or_more_races" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Two or more Races</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="hispanic_or_latino_of_any_race" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Hispanic</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="not_hispanic_or_latino" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="speak_a_language_other_than_english" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent of Population, 5 Years and Over, who Speak a language other than English</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Environmental Justice Layers, by Census Block Group</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Lead Paint</td>
                                       <td style="text-align:center;" >Diesel Particulate</td>
                                       <td style="text-align:center;" >Air Toxics Cancer</td>
                                       <td style="text-align:center;" >Air toxics respiratory</td>
                                       <td style="text-align:center;" >Traffic</td>
                                       <td style="text-align:center;" >Direct Dischargers</td>
                                       <td style="text-align:center;" >National Priorities </td>
                                       <td style="text-align:center;" >Risk Management</td>
                                       <td style="text-align:center;" >Storage and Disposal</td>
                                       <td style="text-align:center;" >Ozone</td>
                                       <td style="text-align:center;" >PM2.5</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu1"></span></td>
                                      <td>&gt;-200.0</td>
                                      <td>&gt;-300.0</td>
                                      <td>&gt;-45000.0</td>
                                      <td>&gt;-600.0</td>
                                      <td>&gt;800000.0</td>
                                      <td>&gt;-47000.0</td>
                                      <td>&gt;-400.0</td>
                                      <td>&gt;-450.0</td>
                                      <td>&gt;-3200.0</td>
                                      <td>&gt;-58000.0</td>
                                      <td>&gt;-11000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu2"></span></td>
                                      <td>&ge; -200.0 &amp; &lt; 0.0</td>
                                      <td>&ge; -300.0 &amp; &lt; 0.0</td>
                                      <td>&ge; -45000.0 &amp; &lt; -20000.0</td>
                                      <td>&ge; -600.0 &amp; &lt; -250</td>
                                      <td>&ge; 800000.0 &amp; &lt; 1700000.0</td>
                                      <td>&ge; -47000.0 &amp; &lt; -35000.0</td>
                                      <td>&ge; -400.0 &amp; &lt; -120.0</td>
                                      <td>&ge; -450.0 &amp; &lt; 1000.0</td>
                                      <td>&ge; -3200.0 &amp; &lt; -1000.0</td>
                                      <td>&ge; -58000.0 &amp; &lt; -28000.0</td>
                                      <td>&ge; -11000.0 &amp; &lt; -5500.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu3"></span></td>
                                      <td>&ge; 0.0 &amp; &lt; 200.0</td>
                                      <td>&ge; 0.0 &amp; &lt; 280.0</td>
                                      <td>&ge; -20000.0 &amp; &lt; 5000.0</td>
                                      <td>&ge; -250.0 &amp; &lt; 100.0</td>
                                      <td>&ge; 1700000.0 &amp; &lt; 1700000.0</td>
                                      <td>&ge; -35000.0 &amp; &lt; -22000.0</td>
                                      <td>&ge; -120.0 &amp; &lt; 150.0</td>
                                      <td>&ge; 1000.0 &amp; &lt; 2450.0</td>
                                      <td>&ge; -1000.0 &amp; &lt; 1800.0</td>
                                      <td>&ge; -28000.0 &amp; &lt; 600.0</td>
                                      <td>&ge; -5500.0 &amp; &lt; 1000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu4"></span></td>
                                      <td>&ge; 200.0 &amp; &lt; 400.0</td>
                                      <td>&ge; 280.0 &amp; &lt; 580.0</td>
                                      <td>&ge; 5000.0 &amp; &lt; 30000.0</td>
                                      <td>&ge; 100.0 &amp; &lt; 450.0</td>
                                      <td>&ge; 2600000.0 &amp; &lt; 2600000.0</td>
                                      <td>&ge; -22000.0 &amp; &lt; -10000.0</td>
                                      <td>&ge; 150.0 &amp; &lt; 420.0</td>
                                      <td>&ge; 2450.0 &amp; &lt; 3900.0</td>
                                      <td>&ge; 1800.0 &amp; &lt; 4600.0</td>
                                      <td>&ge; 600.0 &amp; &lt; 38000.0</td>
                                      <td>&ge; 1000.0 &amp; &lt; 7500.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu5"></span></td>
                                      <td>&ge; 400.0 &amp; &lt; 600.0</td>
                                      <td>&ge; 580.0 &amp; &lt; 850.0</td>
                                      <td>&ge; 30000.0 &amp; &lt; 55000.0</td>
                                      <td>&ge; 450.0 &amp; &lt; 800.0</td>
                                      <td>&ge; 3500000.0 &amp; &lt; 4400000.0</td>
                                      <td>&ge; -10000.0 &amp; &lt; 200.0</td>
                                      <td>&ge; 420.0 &amp; &lt; 690.0</td>
                                      <td>&ge; 3900.0 &amp; &lt; 5350.0</td>
                                      <td>&ge; 4600.0 &amp; &lt; 7300.0</td>
                                      <td>&ge; 38000.0 &amp; &lt; 70000.0</td>
                                      <td>&ge; 7500.0 &amp; &lt; 15000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu6"></span></td>
                                      <td>&ge; 600.0</td>
                                      <td>&ge; 850.0</td>
                                      <td>&ge; 55000.0</td>
                                      <td>&ge; 800.0</td>
                                      <td>&ge; 4400000.0</td>
                                      <td>&ge; 200.0</td>
                                      <td>&ge; 690.0</td>
                                      <td>&ge; 5350.0</td>
                                      <td>&ge; 7300.0</td>
                                      <td>&ge; 70000.0</td>
                                      <td>&ge; 15000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_ldpnt_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for % pre-1960 housing (lead paint indicator)</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_dslpm_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Diesel particulate matter level in air</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_cancr_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Air toxics cancer risk</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_resp_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Air toxics respiratory hazard index</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_ptraf_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Traffic proximity and volume</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_pwdis_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Indicator for major direct dischargers to water</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_pnpl_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Proximity to National Priorities List (NPL) sites</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_prmp_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Proximity to Risk Management Plan (RMP) facilities</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_ptsdf_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_ozone_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Ozone level in air</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="d_pm25_2" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for PM2.5 level in air</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Health Layers, by Zip Code</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Total Cases</td>
                                       <td style="text-align:center;" >Cases Per 10,000 Residents</td>
                                       <td style="text-align:center;" >Cases Per 100,000 Residents</td>
                                       <td style="text-align:center;" >Deaths</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu1"></span></td>
                                      <td>&gt; 1328</td>
                                      <td>&gt; 586.0</td>
                                      <td>&gt; 5859.0</td>
                                      <td>&gt; 17</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu2"></span></td>
                                      <td>&ge; 1328 &amp; &lt; 2656</td>
                                      <td>&ge; 586.0 &amp; &lt; 1172.0</td>
                                      <td>&ge; 5859.0 &amp; &lt; 11718.0</td>
                                      <td>&ge; 17 &amp; &lt; 34</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu3"></span></td>
                                      <td>&ge; 2656 &amp; &lt; 3984</td>
                                      <td>&ge; 1172.0 &amp; &lt; 1758.0</td>
                                      <td>&ge; 11718.0 &amp; &lt; 17577.0</td>
                                      <td>&ge; 34 &amp; &lt; 51</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu4"></span></td>
                                      <td>&ge; 3984 &amp; &lt; 5416</td>
                                      <td>&ge; 1758.0 &amp; &lt; 2344.0</td>
                                      <td>&ge; 17577.0 &amp; &lt; 23436.0</td>
                                      <td>&ge; 51 &amp; &lt; 65</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu5"></span></td>
                                      <td>&ge; 5416 &amp; &lt; 6644</td>
                                      <td>&ge; 2344.0 &amp; &lt; 2930.0</td>
                                      <td>&ge; 23436.0 &amp; &lt; 29295.0</td>
                                      <td>&ge; 65 &amp; &lt; 85</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu6"></span></td>
                                        <td>&ge; 6644</td>
                                        <td>&ge; 2930.0
                                        <td>&ge; 29295.0</td>
                                        <td>&ge; 85</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="cases" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Total Cases</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="cases_per_10000_res" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="cases_per_100000_res" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap1PanelRadioLayer" val="deaths" v-model="currentlayer1" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Deaths</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Ancillary Layers</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina One Map</q-tooltip>
                      <div class="q-pa-md q-gutter-y-sm column">
                        <q-toggle
                          :label="`North Carolina Counties ${ ncCountiesModel1 }`"
                          :key="layers1[4].id"
                          v-on:input="showMap1PanelToggleLayer(layers1)"
                          :class="{ 'is-active': layers1[4].visible }"
                          color="teal"
                          false-value="Not Selected"
                          true-value="Selected"
                          v-model="ncCountiesModel1"
                        />
                      </div>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-separator></q-separator>
                <q-item clickable v-close-popup>
                  <q-item-section>Close</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <q-toolbar-title class="text-black">NC-Enviroscan Dual Map One</q-toolbar-title>
        </q-toolbar>
        <!-- // Map One Toolbar and Menu -->

        <!-- // Map Two Toolbar and Menu -->
        <q-toolbar class="col-5 text-black">
          <q-space />
          <q-btn flat round dense icon="menu" class="q-mr-sm text-black">
            <q-tooltip>Map Two Menu</q-tooltip>
            <q-menu content-class="bg-teal-1">
              <q-list dense style="min-width: 100px">
                <q-item clickable>
                  <q-item-section>Base Layers</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item tag="label" v-ripple>
                        <q-item-section avatar>
                          <q-radio v-on:input="showBaseLayer2" val="osm" v-model="baselayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>OpenStreetMap</q-item-label>
                        </q-item-section>
                      </q-item>
                      <q-item tag="label" v-ripple>
                        <q-item-section avatar>
                          <q-radio v-on:input="showBaseLayer2" val="mapbox" v-model="baselayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>MapBox Satellite</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>

                <q-separator></q-separator>
                <q-item clickable>
                  <q-item-section>NC Well Data Layers, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Arsenic (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Arsenic</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_arsenic_med" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_arsenic_mean" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_arsenic_prcast" v-model="currentlayer2" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu1"></span></td>
                                      <td>&gt; 6.83</td>
                                      <td>&gt; 8.95</td>
                                      <td>&gt; 16.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu2"></span></td>
                                      <td>&ge; 6.83 &amp; &lt; 10.12</td>
                                      <td>&ge; 8.95 &amp; &lt; 14.93</td>
                                      <td>&ge; 16.0 &amp; &lt; 32.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu3"></span></td>
                                      <td>&ge; 10.12 &amp; &lt; 13.42</td>
                                      <td>&ge; 14.93 &amp; &lt; 20.92</td>
                                      <td>&ge; 32.0 &amp; &lt; 48.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu4"></span></td>
                                      <td>&ge; 13.42 &amp; &lt; 16.71</td>
                                      <td>&ge; 20.92 &amp; &lt; 26.9</td>
                                      <td>&ge; 48.0 &amp; &lt; 64.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="assqu5"></span></td>
                                      <td>&ge; 16.71</td>
                                      <td>&ge; 26.9</td>
                                      <td>&ge; 64.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Cadmium (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Cadmium</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_cadmium_med" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_cadmium_mean" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_cadmium_prcast" v-model="currentlayer2" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu1"></span></td>
                                      <td>&gt; 0.74</td>
                                      <td>&gt; 2.71</td>
                                      <td>&gt; 4.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu2"></span></td>
                                      <td>&ge; 0.74 &amp; &lt; 0.77</td>
                                      <td>&ge; 2.71 &amp; &lt; 4.72</td>
                                      <td>&ge; 4.0 &amp; &lt; 8.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu3"></span></td>
                                      <td>&ge; 0.77 &amp; &lt; 0.79</td>
                                      <td>&ge; 4.72 &amp; &lt; 6.72</td>
                                      <td>&ge; 8.0 &amp; &lt; 12.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu4"></span></td>
                                      <td>&ge; 0.79 &amp; &lt; 0.82</td>
                                      <td>&ge; 6.72 &amp; &lt; 8.73</td>
                                      <td>&ge; 12.0 &amp; &lt; 16.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="cdsqu5"></span></td>
                                      <td>&ge; 0.82</td>
                                      <td>&ge; 8.73</td>
                                      <td>&ge; 16.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item dense tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Lead (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Lead</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_lead_med" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_lead_mean" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_lead_prcast" v-model="currentlayer2" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu1"></span></td>
                                      <td>&gt; 11.69</td>
                                      <td>&gt; 39.22</td>
                                      <td>&gt; 20.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu2"></span></td>
                                      <td>&ge; 11.69 &amp; &lt; 19.83</td>
                                      <td>&ge; 39.22 &amp; &lt; 75.53</td>
                                      <td>&ge; 20.0 &amp; &lt; 40.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu3"></span></td>
                                      <td>&ge; 19.83 &amp; &lt; 27.98</td>
                                      <td>&ge; 75.53 &amp; &lt; 111.83</td>
                                      <td>&ge; 40.0 &amp; &lt; 60.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu4"></span></td>
                                      <td>&ge; 27.98 &amp; &lt; 36.12</td>
                                      <td>&ge; 111.83 &amp; &lt; 148.14</td>
                                      <td>&ge; 60.0 &amp; &lt; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqu5"></span></td>
                                      <td>&ge; 36.12</td>
                                      <td>&ge; 148.14</td>
                                      <td>&ge; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="pbsqufill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item dense ag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Maganese (ppb and %)</q-tooltip>
                        <table cellspacing="1" cellpadding="1" style="width:100%">
                          <caption style="text-align:left">Manganese</caption>
                          <tr>
                            <td>Median</td>
                            <td>Mean</td>
                            <td>% of Standard</td>
                          </tr>
                          <tr>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_mng_med" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_mng_mean" v-model="currentlayer2" color="teal" /></td>
                            <td><q-radio v-on:input="showMap2PanelRadioLayer" val="ncwellwise_mng_prcast" v-model="currentlayer2" color="teal" /></td>
                          </tr>
                        </table>
                      </q-item>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Median (ppb)</td>
                                       <td style="text-align:center;" >Mean (ppb)</td>
                                       <td style="text-align:center;" >% of Standard</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu1"></span></td>
                                      <td>&gt; 184.4</td>
                                      <td>&gt; 213.09</td>
                                      <td>&gt; 20.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu2"></span></td>
                                      <td>&ge; 184.4 &amp; &lt; 350.8</td>
                                      <td>&ge; 213.09 &amp; &lt; 404.97</td>
                                      <td>&ge; 20.0 &amp; &lt; 40.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu3"></span></td>
                                      <td>&ge; 350.8 &amp; &lt; 517.2</td>
                                      <td>&ge; 404.97 &amp; &lt; 596.85</td>
                                      <td>&ge; 40.0 &amp; &lt; 60.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu4"></span></td>
                                      <td>&ge; 517.2 &amp; &lt; 683.6</td>
                                      <td>&ge; 596.85 &amp; &lt; 788.73</td>
                                      <td>&ge; 60.0 &amp; &lt; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="mnsqu5"></span></td>
                                      <td>&ge; 683.6</td>
                                      <td>&ge; 788.73</td>
                                      <td>&ge; 80.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Socioeconomic Layers, by Census Tracts</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <tr>
                                  <td style="padding:5px"><span class="acssqu1"></span></td>
                                  <td>&gt; 15%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu2"></span></td>
                                  <td>&ge; 15% &amp; &lt; 30%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu3"></span></td>
                                  <td>&ge; 30% &amp; &lt; 45%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu4"></span></td>
                                  <td>&ge; 45% &amp; &lt; 60%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu5"></span></td>
                                  <td>&ge; 60% &amp; &lt; 75%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="acssqu6"></span></td>
                                  <td>&ge; 75%</td>
                                </tr>
                                <tr>
                                  <td style="padding:5px"><span class="squfill"></span></td>
                                  <td>Fill -999.99</td>
                                </tr>
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="percent_below_poverty_level" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Below the Poverty Level</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="american_indian_and_alaska_native_alone" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Native American</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="asian_alone" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Asian</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="black_or_african_american_alone" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic Black</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="native_hawaiian_and_other_pacific_islander_alone" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic Native Hawaiian and other Pacific Islander</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="white_alone" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic White</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="two_or_more_races" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Two or more Races</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="hispanic_or_latino_of_any_race" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Hispanic</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="not_hispanic_or_latino" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent Non-Hispanic</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From US Census American Community Survey, 2019 5 year estimate</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="speak_a_language_other_than_english" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Percent of Population, 5 Years and Over, who Speak a language other than English</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Environmental Justice Layers, by Census Block Group</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Lead Paint</td>
                                       <td style="text-align:center;" >Diesel Particulate</td>
                                       <td style="text-align:center;" >Air Toxics Cancer</td>
                                       <td style="text-align:center;" >Air toxics respiratory</td>
                                       <td style="text-align:center;" >Traffic</td>
                                       <td style="text-align:center;" >Direct Dischargers</td>
                                       <td style="text-align:center;" >National Priorities </td>
                                       <td style="text-align:center;" >Risk Management</td>
                                       <td style="text-align:center;" >Storage and Disposal</td>
                                       <td style="text-align:center;" >Ozone</td>
                                       <td style="text-align:center;" >PM2.5</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu1"></span></td>
                                      <td>&gt;-200.0</td>
                                      <td>&gt;-300.0</td>
                                      <td>&gt;-45000.0</td>
                                      <td>&gt;-600.0</td>
                                      <td>&gt;800000.0</td>
                                      <td>&gt;-47000.0</td>
                                      <td>&gt;-400.0</td>
                                      <td>&gt;-450.0</td>
                                      <td>&gt;-3200.0</td>
                                      <td>&gt;-58000.0</td>
                                      <td>&gt;-11000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu2"></span></td>
                                      <td>&ge; -200.0 &amp; &lt; 0.0</td>
                                      <td>&ge; -300.0 &amp; &lt; 0.0</td>
                                      <td>&ge; -45000.0 &amp; &lt; -20000.0</td>
                                      <td>&ge; -600.0 &amp; &lt; -250</td>
                                      <td>&ge; 800000.0 &amp; &lt; 1700000.0</td>
                                      <td>&ge; -47000.0 &amp; &lt; -35000.0</td>
                                      <td>&ge; -400.0 &amp; &lt; -120.0</td>
                                      <td>&ge; -450.0 &amp; &lt; 1000.0</td>
                                      <td>&ge; -3200.0 &amp; &lt; -1000.0</td>
                                      <td>&ge; -58000.0 &amp; &lt; -28000.0</td>
                                      <td>&ge; -11000.0 &amp; &lt; -5500.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu3"></span></td>
                                      <td>&ge; 0.0 &amp; &lt; 200.0</td>
                                      <td>&ge; 0.0 &amp; &lt; 280.0</td>
                                      <td>&ge; -20000.0 &amp; &lt; 5000.0</td>
                                      <td>&ge; -250.0 &amp; &lt; 100.0</td>
                                      <td>&ge; 1700000.0 &amp; &lt; 1700000.0</td>
                                      <td>&ge; -35000.0 &amp; &lt; -22000.0</td>
                                      <td>&ge; -120.0 &amp; &lt; 150.0</td>
                                      <td>&ge; 1000.0 &amp; &lt; 2450.0</td>
                                      <td>&ge; -1000.0 &amp; &lt; 1800.0</td>
                                      <td>&ge; -28000.0 &amp; &lt; 600.0</td>
                                      <td>&ge; -5500.0 &amp; &lt; 1000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu4"></span></td>
                                      <td>&ge; 200.0 &amp; &lt; 400.0</td>
                                      <td>&ge; 280.0 &amp; &lt; 580.0</td>
                                      <td>&ge; 5000.0 &amp; &lt; 30000.0</td>
                                      <td>&ge; 100.0 &amp; &lt; 450.0</td>
                                      <td>&ge; 2600000.0 &amp; &lt; 2600000.0</td>
                                      <td>&ge; -22000.0 &amp; &lt; -10000.0</td>
                                      <td>&ge; 150.0 &amp; &lt; 420.0</td>
                                      <td>&ge; 2450.0 &amp; &lt; 3900.0</td>
                                      <td>&ge; 1800.0 &amp; &lt; 4600.0</td>
                                      <td>&ge; 600.0 &amp; &lt; 38000.0</td>
                                      <td>&ge; 1000.0 &amp; &lt; 7500.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu5"></span></td>
                                      <td>&ge; 400.0 &amp; &lt; 600.0</td>
                                      <td>&ge; 580.0 &amp; &lt; 850.0</td>
                                      <td>&ge; 30000.0 &amp; &lt; 55000.0</td>
                                      <td>&ge; 450.0 &amp; &lt; 800.0</td>
                                      <td>&ge; 3500000.0 &amp; &lt; 4400000.0</td>
                                      <td>&ge; -10000.0 &amp; &lt; 200.0</td>
                                      <td>&ge; 420.0 &amp; &lt; 690.0</td>
                                      <td>&ge; 3900.0 &amp; &lt; 5350.0</td>
                                      <td>&ge; 4600.0 &amp; &lt; 7300.0</td>
                                      <td>&ge; 38000.0 &amp; &lt; 70000.0</td>
                                      <td>&ge; 7500.0 &amp; &lt; 15000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="ejssqu6"></span></td>
                                      <td>&ge; 600.0</td>
                                      <td>&ge; 850.0</td>
                                      <td>&ge; 55000.0</td>
                                      <td>&ge; 800.0</td>
                                      <td>&ge; 4400000.0</td>
                                      <td>&ge; 200.0</td>
                                      <td>&ge; 690.0</td>
                                      <td>&ge; 5350.0</td>
                                      <td>&ge; 7300.0</td>
                                      <td>&ge; 70000.0</td>
                                      <td>&ge; 15000.0</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_ldpnt_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for % pre-1960 housing (lead paint indicator)</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_dslpm_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Diesel particulate matter level in air</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_cancr_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Air toxics cancer risk</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_resp_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Air toxics respiratory hazard index</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_ptraf_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Traffic proximity and volume</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_pwdis_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Indicator for major direct dischargers to water</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_pnpl_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Proximity to National Priorities List (NPL) sites</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_prmp_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Proximity to Risk Management Plan (RMP) facilities</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_ptsdf_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Proximity to Treatment Storage and Disposal (TSDF) facilities</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_ozone_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for Ozone level in air</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From the US Environmental Protection Agency</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="d_pm25_2" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>EJ Index for PM2.5 level in air</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Health Layers, by Zip Code</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-item dense tag="label" v-ripple>
                        <!-- // legend -->
                        <div class="q-pa-md q-gutter-y-sm column">
                          LEGEND
                          <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
                            <font size="2" face="Arial" >
                              <q-markup-table dense class="bg-teal-1">
                                <!-- tr>
                                  <td id="nested" -->
                                    <tr>
                                       <td style="text-align:center;" colspan="2">Total Cases</td>
                                       <td style="text-align:center;" >Cases Per 10,000 Residents</td>
                                       <td style="text-align:center;" >Cases Per 100,000 Residents</td>
                                       <td style="text-align:center;" >Deaths</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu1"></span></td>
                                      <td>&gt; 1328</td>
                                      <td>&gt; 586.0</td>
                                      <td>&gt; 5859.0</td>
                                      <td>&gt; 17</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu2"></span></td>
                                      <td>&ge; 1328 &amp; &lt; 2656</td>
                                      <td>&ge; 586.0 &amp; &lt; 1172.0</td>
                                      <td>&ge; 5859.0 &amp; &lt; 11718.0</td>
                                      <td>&ge; 17 &amp; &lt; 34</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu3"></span></td>
                                      <td>&ge; 2656 &amp; &lt; 3984</td>
                                      <td>&ge; 1172.0 &amp; &lt; 1758.0</td>
                                      <td>&ge; 11718.0 &amp; &lt; 17577.0</td>
                                      <td>&ge; 34 &amp; &lt; 51</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu4"></span></td>
                                      <td>&ge; 3984 &amp; &lt; 5416</td>
                                      <td>&ge; 1758.0 &amp; &lt; 2344.0</td>
                                      <td>&ge; 17577.0 &amp; &lt; 23436.0</td>
                                      <td>&ge; 51 &amp; &lt; 65</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu5"></span></td>
                                      <td>&ge; 5416 &amp; &lt; 6644</td>
                                      <td>&ge; 2344.0 &amp; &lt; 2930.0</td>
                                      <td>&ge; 23436.0 &amp; &lt; 29295.0</td>
                                      <td>&ge; 65 &amp; &lt; 85</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="heasqu6"></span></td>
                                        <td>&ge; 6644</td>
                                        <td>&ge; 2930.0
                                        <td>&ge; 29295.0</td>
                                        <td>&ge; 85</td>
                                    </tr>
                                    <tr>
                                      <td style="padding:5px"><span class="squfill"></span></td>
                                      <td>Fill -999.99</td>
                                    </tr>
                                  <!-- /td>
                                </tr -->
                              </q-markup-table>
                            </font>
                          </q-popup-proxy>
                        </div>
                        <!-- // legend -->
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="cases" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Total Cases</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="cases_per_10000_res" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Cases Per 10,000 Residents</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="cases_per_100000_res" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Cases Per 100,000 Residents-</q-item-label>
                        </q-item-section>
                      </q-item>

                      <q-item tag="label" v-ripple>
                        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina Department of Health and Human Services</q-tooltip>
                        <q-item-section avatar>
                          <q-radio v-on:input="showMap2PanelRadioLayer" val="deaths" v-model="currentlayer2" color="teal" />
                        </q-item-section>
                        <q-item-section>
                          <q-item-label>Covid-19 Deaths</q-item-label>
                        </q-item-section>
                      </q-item>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-item clickable>
                  <q-item-section>Ancillary Layers</q-item-section>
                  <q-item-section side>
                    <q-icon name="keyboard_arrow_right"></q-icon>
                  </q-item-section>

                  <q-menu anchor="top end" self="top start" content-class="bg-teal-1">
                    <q-list>
                      <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">From North Carolina One Map</q-tooltip>
                      <div class="q-pa-md q-gutter-y-sm column">
                        <q-toggle
                          :label="`North Carolina Counties ${ ncCountiesModel2 }`"
                          :key="layers2[4].id"
                          v-on:input="showMap2PanelToggleLayer(layers2)"
                          :class="{ 'is-active': layers2[4].visible }"
                          color="teal"
                          false-value="Not Selected"
                          true-value="Selected"
                          v-model="ncCountiesModel2"
                        />
                      </div>
                    </q-list>
                  </q-menu>
                </q-item>
                <q-separator></q-separator>
                <q-item clickable v-close-popup>
                  <q-item-section>Close</q-item-section>
                </q-item>
              </q-list>
            </q-menu>
          </q-btn>
          <q-toolbar-title class="text-black">NC-Enviroscan Dual Map Two</q-toolbar-title>
        </q-toolbar>
        <!-- // Map Two Toolbar and Menu -->
        </div>
      </q-header>

      <div class="wrapper">
        <!--// app map1 -->
        <vl-map v-if="mapVisible" class="dualmap" ref="map1" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
          data-projection="EPSG:4326" @mounted="onMapMounted" :controls="false" style="height:1200px">
          <!--//map1 view aka ol.View -->
          <vl-view ref="view" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>
            <!--// base layers -->
            <vl-layer-tile v-for="layer in baseLayers1" :key="layer.name" :id="layer.name" :visible="layer.visible">
              <component ref="baselayer1" :is="'vl-source-' + layer.name" v-bind="layer"></component>
            </vl-layer-tile>
            <!--// base layers1 -->

            <!--// other layers1 from config -->
            <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
            <vl-layer-vector-tile v-for="layer in layers1" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
              <!--// add vl-source-* -->
              <component :is="layer.source.cmp" v-bind="layer.source" ref="layer1Source" />
              <!--// add style components if provided -->
              <!--// create vl-style-box or vl-style-func -->
              <component v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" ref="layer1Style" />
            </vl-layer-vector-tile>
            <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
            <!--// other layers1 -->
        </vl-map>
        <!--// app map1 -->

        <!--// app map2 -->
        <vl-map v-if="mapVisible" class="dualmap" ref="map2" :load-tiles-while-animating="true" :load-tiles-while-interacting="true"
          data-projection="EPSG:4326" @mounted="onMapMounted" :controls="false" style="height:1200px">
           <!--// map2 view aka ol.View -->
          <vl-view ref="view" :center.sync="center" :zoom.sync="zoom" :rotation.sync="rotation"></vl-view>
          <!--// base layers2 -->
          <vl-layer-tile v-for="layer in baseLayers2" :key="layer.name" :id="layer.name" :visible="layer.visible">
            <component  ref="baselayer2" :is="'vl-source-' + layer.name" v-bind="layer"></component>
          </vl-layer-tile>
          <!--// base layers2 -->

          <!--// other layers2 from config -->
          <!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <vl-layer-vector-tile v-for="layer in layers2" :is="layer.cmp" v-if="layer.visible" :key="layer.id" v-bind="layer">
            <!--// add vl-source-* -->
            <component ref="layer2Source" :is="layer.source.cmp" v-bind="layer.source" />
            <!--// add style components if provided -->
            <!--// create vl-style-box or vl-style-func -->
            <component ref="layer2Style" v-if="layer.style" v-for="(style, i) in layer.style" :key="i" :is="style.cmp" v-bind="style" />
          </vl-layer-vector-tile>
          <!-- eslint-enable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
          <!--// other layers2 -->
        </vl-map>
        <!--// app map2 -->
      </div>

      <!--// Go to Single Screen Map button -->
        <q-page-sticky position="top-left" :offset="[58, 18]">
        <q-btn flat round dense icon="fas fa-sign-out-alt" class="bg-teal text-black" aria-label="Single Screen Map" @click="$router.replace('/')">
          <q-tooltip>Go to Single Screen Map</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <!--// Go to Single Screen Map button -->

      <!--// ol map1 controls -->
      <!-- q-page-sticky position="top-left" :offset="[18, 58]">
        <div id="Zoom1Target"></div>
      </q-page-sticky -->
      <q-page-sticky position="bottom-left" :offset="[8, 38]">
        <div id="OverviewMap1Target"></div>
      </q-page-sticky>
      <q-page-sticky position="bottom-left" :offset="[15, 8]">
        <div id="Scale1Target"></div>
      </q-page-sticky>
      <!--// ol map1 controls -->

      <!--// Fullscreen button -->
      <q-page-sticky position="top-right" :offset="[18, 18]">
        <q-btn color="teal" class="text-black" @click="$q.fullscreen.toggle()" round :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'">
          <q-tooltip>Open &amp; Close Full Screen</q-tooltip>
        </q-btn>
      </q-page-sticky>
      <!--// Fullscreen button -->

      <!--// select location tool -->
      <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-tooltip anchor="center left" self="center right" :offset="[10, 10]">Tools</q-tooltip>
        <q-fab icon="keyboard_arrow_up" direction="up" color="teal text-black">
          <q-tooltip anchor="top left" self="top right" :offset="[10, 10]">Change Location</q-tooltip>
          <q-fab-action color="teal" class="text-black" icon="fas fa-map-marked-alt">
            <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
              <q-card class="bg-teal-1">
                <q-banner inline-actions class="bg-teal-1">
                  <div class="q-pa-md" style="max-width: 400px">
                    <q-form @submit="address2Geoloc" @reset="resetAddress" class="q-gutter-md">
                      <q-input filled v-model="address" label="Address *" hint="Address, City, State and Country" lazy-rules
                        :rules="[ val => val && val.length > 0 || 'Please type something']"
                      ></q-input>
                      <div>
                        <q-btn label="Submit" type="submit" color="teal"></q-btn>
                        <q-btn label="Reset" type="reset" color="teal" flat class="q-ml-sm"></q-btn>
                      </div>
                    </q-form>
                  </div>
                  <template align="right" v-slot:action>
                    <q-btn flat round dense icon="close" color="teal" v-close-popup />
                  </template>
                </q-banner>
                <q-separator />
              </q-card>
            </q-popup-proxy>
          </q-fab-action>
        </q-fab>
      </q-page-sticky>
      <!--// select location tool -->

      <!--// base layer map attribution -->
      <q-page-sticky position="bottom-left" :offset="[200, 38]">
        <div id="AttributionTarget"></div>
      </q-page-sticky>
      <!--// base layer map attribution -->
    </q-page-container>
  </q-layout>
</template>

<script>
// quasar and vuelayers import
import { openURL } from 'quasar'
// import { findPointOnSurface, createStyle } from 'vuelayers/lib/ol-ext'
import { createStyle } from 'vuelayers/lib/ol-ext'
import { camelCase } from 'lodash'

// ol controls import
import ScaleLine from 'ol/control/ScaleLine'
import OverviewMap from 'ol/control/OverviewMap'
import Zoom from 'ol/control/Zoom'
import Attribution from 'ol/control/Attribution'

// other ol imports
import { Style, Stroke, Fill } from 'ol/style'
import { DEVICE_PIXEL_RATIO } from 'ol/has.js'

// geocoder
const Nominatim = require('nominatim-geocoder')
const geocoder = new Nominatim()

// pubhost and secrets import
import pubhost from '../assets/pubhost.json'
import secrets from '../assets/secrets.json'

let gettoken = function () {
  return secrets[0].MB_KEY
}

export default {
  name: 'NC-Enviroscan-Dual',
  components: {
  },
  data () {
    return {
      // map parameters
      // center: [-73.845, 40.72],
      center: [NaN, NaN],
      zoom: 9,
      rotation: 0,
      mapVisible: true,
      // Other layers attributes
      ncCountiesModel1: 'Not Selected',
      ncCountiesModel2: 'Not Selected',
      address: null,
      acceptaddress: false,
      vtSelection: {},
      vtIdProp: 'geoid10',
      // baselayers config
      baselayer1: 'osm',
      baselayer2: 'osm',
      baseLayers1: [
        {
          name: 'osm',
          title: 'OpenStreetMap',
          visible: true
        },
        {
          name: 'mapbox',
          title: 'Mapbox Satellite',
          // mapId: 'mapbox.mapbox-streets-v7',
          mapId: 'mapbox.satellite',
          accessToken: gettoken(),
          visible: false
        }
      ],
      baseLayers2: [
        {
          name: 'osm',
          title: 'OpenStreetMap',
          visible: true
        },
        {
          name: 'mapbox',
          title: 'Mapbox Satellite',
          // mapId: 'mapbox.mapbox-streets-v7',
          mapId: 'mapbox.satellite',
          accessToken: gettoken(),
          visible: false
        }
      ],
      // layers config
      currentlayer1: 'ncwellwise_arsenic_med',
      currentlayer2: 'ncwellwise_arsenic_med',
      layers1: [
        {
          id: this.getNCWellwiseLayer1ID(),
          title: 'NC Wellwise Layer 1',
          // cmp: 'vl-layer-vector',
          cmp: 'vl-layer-vector-tile',
          visible: true,
          source: {
            // cmp: 'vl-source-vector',
            cmp: 'vl-source-vector-tile',
            // url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseStyle1
            }
          ]
        },
        {
          id: this.getACSCensusLayer1ID(),
          title: 'ACS Census',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/acs_2019_5y_estimates_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getacsStyle1
            }
          ]
        },
        {
          id: this.getEJScreenLayer1ID(),
          title: 'EJScreen',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ejscreen_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getejscreenStyle1
            }
          ]
        },
        {
          id: this.getCovid19Layer1ID(),
          title: 'Covid19',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/nc_covid_zipcode_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getcovid19Style1
            }
          ]
        },
        {
          id: 'ncCounties1',
          title: 'NC Counties1',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncdot_county_boundaries.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getNCCountiesStyle1
            }
          ]
        },
        {
          id: 'triwellwise_arsenic_max',
          title: 'triangle wellwise Arsenic Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_triangle_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseArsenicMaxStyle
            }
          ]
        },
        {
          id: 'triwellwise_cadmium_max',
          title: 'Triangle Wellwise Cadmium Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_triangle_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseCadmiumMaxStyle
            }
          ]
        }
      ],
      layers2: [
        {
          id: this.getNCWellwiseLayer2ID(),
          title: 'NC Wellwise Layer 2',
          // cmp: 'vl-layer-vector',
          cmp: 'vl-layer-vector-tile',
          visible: true,
          source: {
            // cmp: 'vl-source-vector',
            cmp: 'vl-source-vector-tile',
            // url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncwellwise_subset_20102019_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseStyle2
            }
          ]
        },
        {
          id: this.getACSCensusLayer2ID(),
          title: 'ACS Census',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/acs_2019_5y_estimates_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getacsStyle2
            }
          ]
        },
        {
          id: this.getEJScreenLayer2ID(),
          title: 'EJScreen',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ejscreen_subset_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getejscreenStyle2
            }
          ]
        },
        {
          id: this.getCovid19Layer2ID(),
          title: 'Covid19',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/nc_covid_zipcode_geom.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getcovid19Style2
            }
          ]
        },
        {
          id: 'ncCounties2',
          title: 'NC Counties2',
          cmp: 'vl-layer-vector-tile',
          visible: false,
          source: {
            cmp: 'vl-source-vector-tile',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/apimvt/v1/data/ncdot_county_boundaries.mvt?tile={z}/{x}/{y}'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getNCCountiesStyle2
            }
          ]
        },
        {
          id: 'triwellwise_lead_max',
          title: 'Triangle wellwise Lead Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseLeadMaxStyle
            }
          ]
        },
        {
          id: 'triwellwise_mng_max',
          title: 'Triangle Wellwise Manganese Maximum',
          cmp: 'vl-layer-vector',
          visible: false,
          source: {
            cmp: 'vl-source-vector',
            url: 'http://' + pubhost[0].PUBHOST_URL + '/drf/api/ncwellwise_subset_20102019_geom/?format=json'
          },
          style: [
            {
              cmp: 'vl-style-func',
              factory: this.getncwellwiseMngMaxStyle
            }
          ]
        }
      ]
    }
  },
  created: function () {
    // get current location, and use it for map center
    this.$getLocation()
      .then(coordinates => {
        this.center = [coordinates.lng, coordinates.lat]
      })
  },
  methods: {
    openURL,
    camelCase,
    address2Geoloc () {
      // 1 East Edenton St, Raleigh, NC, USA
      geocoder.search({ q: this.address })
        .then((response) => {
          this.center = [Number(response[0].lon), Number(response[0].lat)]
        })
        .catch((error) => {
          console.log(error)
        })
    },
    resetAddress () {
      this.address = null
      this.acceptaddress = false
    },
    getncwellwiseStyle1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        // console.log(selected)
        let data = feature.getProperties()
        let color
        if (this.currentlayer1 === 'ncwellwise_arsenic_med') {
          if (data.arsenic_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_med < 6.83) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_med >= 6.83 && data.arsenic_med < 10.12) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 10.12 && data.arsenic_med < 13.42) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 13.42 && data.arsenic_med < 16.71) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 16.71) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_arsenic_mean') {
          if (data.arsenic_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_mean < 8.95) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_mean >= 8.95 && data.arsenic_mean < 14.93) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 14.93 && data.arsenic_mean < 20.93) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 20.93 && data.arsenic_mean < 26.9) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 26.9) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_arsenic_prcast') {
          if (data.arsenic_prcast === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_prcast < 16.0) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_prcast >= 16.0 && data.arsenic_prcast < 32.0) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_prcast >= 32.0 && data.arsenic_prcast < 48.0) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_prcast >= 48.0 && data.arsenic_prcast < 64.0) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_prcast >= 64.0) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_cadmium_med') {
          if (data.cadmium_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_med < 0.74) {
            color = 'rgba(223, 235, 52, 0.65)'
          } else if (data.cadmium_med >= 0.74 && data.cadmium_med < 77.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_med >= 0.77 && data.cadmium_med < 0.79) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_med >= 0.79 && data.cadmium_med < 0.82) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_med >= 0.82) {
            color = 'rgba(235, 89, 52, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_cadmium_mean') {
          if (data.cadmium_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_mean < 2.71) {
            color = 'rgba(223, 235, 52, 0.65)'
          } else if (data.cadmium_mean >= 2.71 && data.cadmium_mean < 4.72) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_mean >= 4.72 && data.cadmium_mean < 6.72) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_mean >= 6.71 && data.cadmium_mean < 8.73) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_mean >= 8.73) {
            color = 'rgba(235, 89, 52, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_cadmium_prcast') {
          if (data.cadmium_prcast === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_prcast < 4.0) {
            color = 'rgba(223, 235, 52, 0.65)'
          } else if (data.cadmium_prcast >= 4.0 && data.cadmium_prcast < 8.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_prcast >= 8.0 && data.cadmium_prcast < 12.0) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_prcast >= 12.0 && data.cadmium_prcast < 16.0) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_prcast >= 16.0) {
            color = 'rgba(235, 89, 52, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_lead_med') {
          if (data.lead_med === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_med < 11.69) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_med >= 11.69 && data.lead_med < 30.0) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_med >= 19.83 && data.lead_med < 50.0) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_med >= 27.98 && data.lead_med < 80.0) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_med >= 36.12) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_lead_mean') {
          if (data.lead_mean === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_mean < 39.22) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_mean >= 39.22 && data.lead_mean < 75.53) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_mean >= 75.53 && data.lead_mean < 111.83) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_mean >= 111.93 && data.lead_mean < 148.14) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_mean >= 148.14) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_lead_prcast') {
          if (data.lead_prcast === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_prcast < 20.0) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_prcast >= 20.0 && data.lead_prcast < 40.0) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_prcast >= 40.0 && data.lead_prcast < 60.0) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_prcast >= 60.0 && data.lead_prcast < 80.0) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_prcast >= 80.0) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_mng_med') {
          if (data.manganese_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_med < 184.4) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_med >= 184.4 && data.manganese_med < 350.8) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_med >= 350.8 && data.manganese_med < 517.2) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_med >= 517.2 && data.manganese_med < 683.6) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_med >= 683.6) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_mng_mean') {
          if (data.manganese_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_mean < 213.09) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_mean >= 213.09 && data.manganese_mean < 404.97) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_mean >= 404.97 && data.manganese_mean < 596.85) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_mean >= 596.85 && data.manganese_mean < 788.73) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_mean >= 788.73) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        } else if (this.currentlayer1 === 'ncwellwise_mng_prcast') {
          if (data.manganese_prcast === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_prcast < 20.0) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_prcast >= 20.0 && data.manganese_prcast < 40.0) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_prcast >= 40.0 && data.manganese_prcast < 60.0) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_prcast >= 60.0 && data.manganese_prcast < 80.0) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_prcast >= 80.0) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getacsStyle1: function () {
      // console.log(this.currentlayer)
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (data[this.currentlayer1] === -999.99) {
          color = 'rgba(91, 95, 99, 0.65)'
        } else if (data[this.currentlayer1] < 15) {
          color = 'rgba(252, 210, 211, 0.65)'
        } else if (data[this.currentlayer1] >= 15 && data[this.currentlayer1] < 30) {
          color = 'rgba(252, 109, 114, 0.65)'
        } else if (data[this.currentlayer1] >= 30 && data[this.currentlayer1] < 45) {
          color = 'rgba(247, 59, 66, 0.65)'
        } else if (data[this.currentlayer1] >= 45 && data[this.currentlayer1] < 60) {
          color = 'rgba(250, 2, 11, 0.65)'
        } else if (data[this.currentlayer1] >= 60 && data[this.currentlayer1] < 75) {
          color = 'rgba(181, 2, 6, 0.65)'
        } else if (data[this.currentlayer1] >= 75) {
          color = 'rgba(140, 1, 5, 0.65)'
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getejscreenStyle1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer1 === 'd_ldpnt_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -200.0 && data[this.currentlayer1] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 0.0 && data[this.currentlayer1] < 200.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 200.0 && data[this.currentlayer1] < 400.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 400.0 && data[this.currentlayer1] < 600.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 600.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_dslpm_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -300.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -300.0 && data[this.currentlayer1] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 0.0 && data[this.currentlayer1] < 280.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 280.0 && data[this.currentlayer1] < 580.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 580.0 && data[this.currentlayer1] < 850.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 850.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_cancr_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -45000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -45000.0 && data[this.currentlayer1] < -20000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -20000.0 && data[this.currentlayer1] < 5000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 5000.0 && data[this.currentlayer1] < 30000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 30000.0 && data[this.currentlayer1] < 55000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 55000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_resp_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -600.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -600.0 && data[this.currentlayer1] < -250) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -250.0 && data[this.currentlayer1] < 100.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 100.0 && data[this.currentlayer1] < 450.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 450.0 && data[this.currentlayer1] < 800.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 800.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_ptraf_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 800000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 800000.0 && data[this.currentlayer1] < 1700000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1700000.0 && data[this.currentlayer1] < 1700000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 2600000.0 && data[this.currentlayer1] < 2600000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 3500000.0 && data[this.currentlayer1] < 4400000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 4400000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_pwdis_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -47000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -47000.0 && data[this.currentlayer1] < -35000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -35000.0 && data[this.currentlayer1] < -22000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -22000.0 && data[this.currentlayer1] < -10000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -10000.0 && data[this.currentlayer1] < 200.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 200.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_pnpl_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -400.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -400.0 && data[this.currentlayer1] < -120.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -120.0 && data[this.currentlayer1] < 150.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 150.0 && data[this.currentlayer1] < 420.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 420.0 && data[this.currentlayer1] < 690.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 690.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_prmp_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -450.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -450.0 && data[this.currentlayer1] < 1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1000.0 && data[this.currentlayer1] < 2450.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 2450.0 && data[this.currentlayer1] < 3900.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 3900.0 && data[this.currentlayer1] < 5350.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 5350.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_ptsdf_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -3200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -3200.0 && data[this.currentlayer1] < -1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -1000.0 && data[this.currentlayer1] < 1800.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1800.0 && data[this.currentlayer1] < 4600.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 4600.0 && data[this.currentlayer1] < 7300.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 7300.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_ozone_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -58000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -58000.0 && data[this.currentlayer1] < -28000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -28000.0 && data[this.currentlayer1] < 600.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 600.0 && data[this.currentlayer1] < 38000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 38000.0 && data[this.currentlayer1] < 70000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 70000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer1 === 'd_pm25_2') {
          if (data[this.currentlayer1] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < -11000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -11000.0 && data[this.currentlayer1] < -5500.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer1] >= -5500.0 && data[this.currentlayer1] < 1000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 1000.0 && data[this.currentlayer1] < 7500.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 7500.0 && data[this.currentlayer1] < 15000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer1] >= 15000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getcovid19Style1: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer1 === 'cases') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 1328) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 1328 && data[this.currentlayer1] < 2656) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 2656 && data[this.currentlayer1] < 3984) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 3984 && data[this.currentlayer1] < 5416) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 5416 && data[this.currentlayer1] < 6644) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 6644) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer1 === 'cases_per_10000_res') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 586.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 586.0 && data[this.currentlayer1] < 1172.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 1172.0 && data[this.currentlayer1] < 1758.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 1758.0 && data[this.currentlayer1] < 2344.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 2344.0 && data[this.currentlayer1] < 2930.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 2930.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer1 === 'cases_per_100000_res') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 5859.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 5859.0 && data[this.currentlayer1] < 11718.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 11718.0 && data[this.currentlayer1] < 17577.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 17577.0 && data[this.currentlayer1] < 23436.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 23436.0 && data[this.currentlayer1] < 29295.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 29295.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer1 === 'deaths') {
          if (data[this.currentlayer1] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer1] < 17) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer1] >= 17 && data[this.currentlayer1] < 34) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 34 && data[this.currentlayer1] < 51) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer1] >= 51 && data[this.currentlayer1] < 65) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 65 && data[this.currentlayer1] < 85) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer1] >= 85) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getncwellwiseStyle2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        // console.log(selected)
        let data = feature.getProperties()
        let color
        if (this.currentlayer2 === 'ncwellwise_arsenic_med') {
          if (data.arsenic_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_med < 6.83) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_med >= 6.83 && data.arsenic_med < 10.12) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 10.12 && data.arsenic_med < 13.42) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 13.42 && data.arsenic_med < 16.71) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_med >= 16.71) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_arsenic_mean') {
          if (data.arsenic_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_mean < 8.95) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_mean >= 8.95 && data.arsenic_mean < 14.93) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 14.93 && data.arsenic_mean < 20.93) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 20.93 && data.arsenic_mean < 26.9) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_mean >= 26.9) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_arsenic_prcast') {
          if (data.arsenic_prcast === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.arsenic_prcast < 16.0) {
            color = 'rgba(235, 52, 220, 0.65)'
          } else if (data.arsenic_prcast >= 16.0 && data.arsenic_prcast < 32.0) {
            color = 'rgba(186, 52, 235, 0.65)'
          } else if (data.arsenic_prcast >= 32.0 && data.arsenic_prcast < 48.0) {
            color = 'rgba(165, 52, 235, 0.65)'
          } else if (data.arsenic_prcast >= 48.0 && data.arsenic_prcast < 64.0) {
            color = 'rgba(143, 52, 235, 0.65)'
          } else if (data.arsenic_prcast >= 64.0) {
            color = 'rgba(119, 52, 235, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_cadmium_med') {
          if (data.cadmium_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_med < 0.74) {
            color = 'rgba(223, 235, 52, 0.65)'
          } else if (data.cadmium_med >= 0.74 && data.cadmium_med < 77.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_med >= 0.77 && data.cadmium_med < 0.79) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_med >= 0.79 && data.cadmium_med < 0.82) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_med >= 0.82) {
            color = 'rgba(235, 89, 52, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_cadmium_mean') {
          if (data.cadmium_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_mean < 2.71) {
            color = 'rgba(223, 235, 52, 0.65)'
          } else if (data.cadmium_mean >= 2.71 && data.cadmium_mean < 4.72) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_mean >= 4.72 && data.cadmium_mean < 6.72) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_mean >= 6.71 && data.cadmium_mean < 8.73) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_mean >= 8.73) {
            color = 'rgba(235, 89, 52, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_cadmium_prcast') {
          if (data.cadmium_prcast === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.cadmium_prcast < 4.0) {
            color = 'rgba(223, 235, 52, 0.65)'
          } else if (data.cadmium_prcast >= 4.0 && data.cadmium_prcast < 8.0) {
            color = 'rgba(235, 192, 52, 0.65)'
          } else if (data.cadmium_prcast >= 8.0 && data.cadmium_prcast < 12.0) {
            color = 'rgba(235, 162, 52, 0.65)'
          } else if (data.cadmium_prcast >= 12.0 && data.cadmium_prcast < 16.0) {
            color = 'rgba(235, 131, 52, 0.65)'
          } else if (data.cadmium_prcast >= 16.0) {
            color = 'rgba(235, 89, 52, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_lead_med') {
          if (data.lead_med === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_med < 11.69) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_med >= 11.69 && data.lead_med < 30.0) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_med >= 19.83 && data.lead_med < 50.0) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_med >= 27.98 && data.lead_med < 80.0) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_med >= 36.12) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_lead_mean') {
          if (data.lead_mean === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_mean < 39.22) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_mean >= 39.22 && data.lead_mean < 75.53) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_mean >= 75.53 && data.lead_mean < 111.83) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_mean >= 111.93 && data.lead_mean < 148.14) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_mean >= 148.14) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_lead_prcast') {
          if (data.lead_prcast === -999.99) {
            color = 'rgba(50, 110, 219, 0.65)'
          } else if (data.lead_prcast < 20.0) {
            color = 'rgba(196, 200, 207, 0.65)'
          } else if (data.lead_prcast >= 20.0 && data.lead_prcast < 40.0) {
            color = 'rgba(156, 162, 173, 0.65)'
          } else if (data.lead_prcast >= 40.0 && data.lead_prcast < 60.0) {
            color = 'rgba(116, 121, 130, 0.65)'
          } else if (data.lead_prcast >= 60.0 && data.lead_prcast < 80.0) {
            color = 'rgba(79, 82, 89, 0.65)'
          } else if (data.lead_prcast >= 80.0) {
            color = 'rgba(39, 40, 43, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_mng_med') {
          if (data.manganese_med === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_med < 184.4) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_med >= 184.4 && data.manganese_med < 350.8) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_med >= 350.8 && data.manganese_med < 517.2) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_med >= 517.2 && data.manganese_med < 683.6) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_med >= 683.6) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_mng_mean') {
          if (data.manganese_mean === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_mean < 213.09) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_mean >= 213.09 && data.manganese_mean < 404.97) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_mean >= 404.97 && data.manganese_mean < 596.85) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_mean >= 596.85 && data.manganese_mean < 788.73) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_mean >= 788.73) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        } else if (this.currentlayer2 === 'ncwellwise_mng_prcast') {
          if (data.manganese_prcast === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data.manganese_prcast < 20.0) {
            color = 'rgba(194, 232, 190, 0.65)'
          } else if (data.manganese_prcast >= 20.0 && data.manganese_prcast < 40.0) {
            color = 'rgba(81, 222, 67, 0.65)'
          } else if (data.manganese_prcast >= 40.0 && data.manganese_prcast < 60.0) {
            color = 'rgba(25, 128, 11, 0.65)'
          } else if (data.manganese_prcast >= 60.0 && data.manganese_prcast < 80.0) {
            color = 'rgba(14, 82, 5, 0.65)'
          } else if (data.manganese_prcast >= 80.0) {
            color = 'rgba(5, 97, 76, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getacsStyle2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (data[this.currentlayer2] === -999.99) {
          color = 'rgba(91, 95, 99, 0.65)'
        } else if (data[this.currentlayer2] < 15) {
          color = 'rgba(252, 210, 211, 0.65)'
        } else if (data[this.currentlayer2] >= 15 && data[this.currentlayer2] < 30) {
          color = 'rgba(252, 109, 114, 0.65)'
        } else if (data[this.currentlayer2] >= 30 && data[this.currentlayer2] < 45) {
          color = 'rgba(247, 59, 66, 0.65)'
        } else if (data[this.currentlayer2] >= 45 && data[this.currentlayer2] < 60) {
          color = 'rgba(250, 2, 11, 0.65)'
        } else if (data[this.currentlayer2] >= 60 && data[this.currentlayer2] < 75) {
          color = 'rgba(181, 2, 6, 0.65)'
        } else if (data[this.currentlayer2] >= 75) {
          color = 'rgba(140, 1, 5, 0.65)'
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })
          /* createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 8.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel',
            fillColor: color
          }) */
        ]
      }
    },
    getejscreenStyle2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer2 === 'd_ldpnt_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -200.0 && data[this.currentlayer2] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 0.0 && data[this.currentlayer2] < 200.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 200.0 && data[this.currentlayer2] < 400.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 400.0 && data[this.currentlayer2] < 600.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 600.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_dslpm_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -300.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -300.0 && data[this.currentlayer2] < 0.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 0.0 && data[this.currentlayer2] < 280.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 280.0 && data[this.currentlayer2] < 580.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 580.0 && data[this.currentlayer2] < 850.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 850.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_cancr_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -45000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -45000.0 && data[this.currentlayer2] < -20000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -20000.0 && data[this.currentlayer2] < 5000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 5000.0 && data[this.currentlayer2] < 30000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 30000.0 && data[this.currentlayer2] < 55000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 55000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_resp_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -600.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -600.0 && data[this.currentlayer2] < -250) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -250.0 && data[this.currentlayer2] < 100.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 100.0 && data[this.currentlayer2] < 450.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 450.0 && data[this.currentlayer2] < 800.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 800.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_ptraf_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 800000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 800000.0 && data[this.currentlayer2] < 1700000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1700000.0 && data[this.currentlayer2] < 1700000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 2600000.0 && data[this.currentlayer2] < 2600000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 3500000.0 && data[this.currentlayer2] < 4400000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 4400000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_pwdis_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -47000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -47000.0 && data[this.currentlayer2] < -35000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -35000.0 && data[this.currentlayer2] < -22000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -22000.0 && data[this.currentlayer2] < -10000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -10000.0 && data[this.currentlayer2] < 200.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 200.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_pnpl_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -400.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -400.0 && data[this.currentlayer2] < -120.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -120.0 && data[this.currentlayer2] < 150.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 150.0 && data[this.currentlayer2] < 420.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 420.0 && data[this.currentlayer2] < 690.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 690.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_prmp_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -450.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -450.0 && data[this.currentlayer2] < 1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1000.0 && data[this.currentlayer2] < 2450.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 2450.0 && data[this.currentlayer2] < 3900.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 3900.0 && data[this.currentlayer2] < 5350.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 5350.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_ptsdf_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -3200.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -3200.0 && data[this.currentlayer2] < -1000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -1000.0 && data[this.currentlayer2] < 1800.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1800.0 && data[this.currentlayer2] < 4600.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 4600.0 && data[this.currentlayer2] < 7300.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 7300.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_ozone_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -58000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -58000.0 && data[this.currentlayer2] < -28000.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -28000.0 && data[this.currentlayer2] < 600.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 600.0 && data[this.currentlayer2] < 38000.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 38000.0 && data[this.currentlayer2] < 70000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 70000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        } else if (this.currentlayer2 === 'd_pm25_2') {
          if (data[this.currentlayer2] === -99999.9999) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < -11000.0) {
            color = 'rgba(235, 252, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -11000.0 && data[this.currentlayer2] < -5500.0) {
            color = 'rgba(252, 227, 3, 0.65)'
          } else if (data[this.currentlayer2] >= -5500.0 && data[this.currentlayer2] < 1000.0) {
            color = 'rgba(252, 186, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 1000.0 && data[this.currentlayer2] < 7500.0) {
            color = 'rgba(252, 128, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 7500.0 && data[this.currentlayer2] < 15000.0) {
            color = 'rgba(252, 82, 3, 0.65)'
          } else if (data[this.currentlayer2] >= 15000.0) {
            color = 'rgba(140, 1, 5, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })

        ]
      }
    },
    getcovid19Style2: function () {
      return feature => {
        let selected = !!this.vtSelection[feature.get(this.vtIdProp)]
        let data = feature.getProperties()
        let color
        if (this.currentlayer2 === 'cases') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 1328) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 1328 && data[this.currentlayer2] < 2656) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 2656 && data[this.currentlayer2] < 3984) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 3984 && data[this.currentlayer2] < 5416) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 5416 && data[this.currentlayer2] < 6644) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 6644) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer2 === 'cases_per_10000_res') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 586.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 586.0 && data[this.currentlayer2] < 1172.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 1172.0 && data[this.currentlayer2] < 1758.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 1758.0 && data[this.currentlayer2] < 2344.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 2344.0 && data[this.currentlayer2] < 2930.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 2930.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer2 === 'cases_per_100000_res') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 5859.0) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 5859.0 && data[this.currentlayer2] < 11718.0) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 11718.0 && data[this.currentlayer2] < 17577.0) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 17577.0 && data[this.currentlayer2] < 23436.0) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 23436.0 && data[this.currentlayer2] < 29295.0) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 29295.0) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        } else if (this.currentlayer2 === 'deaths') {
          if (data[this.currentlayer2] === -999.99) {
            color = 'rgba(91, 95, 99, 0.65)'
          } else if (data[this.currentlayer2] < 17) {
            color = 'rgba(34, 240, 219, 0.65)'
          } else if (data[this.currentlayer2] >= 17 && data[this.currentlayer2] < 34) {
            color = 'rgba(34, 223, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 34 && data[this.currentlayer2] < 51) {
            color = 'rgba(34, 185, 240, 0.65)'
          } else if (data[this.currentlayer2] >= 51 && data[this.currentlayer2] < 65) {
            color = 'rgba(22, 141, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 65 && data[this.currentlayer2] < 85) {
            color = 'rgba(22, 74, 245, 0.65)'
          } else if (data[this.currentlayer2] >= 85) {
            color = 'rgba(23, 2, 247, 0.65)'
          }
        }
        return [
          new Style({
            stroke: new Stroke({
              color: selected ? 'rgba(200,20,20,0.8)' : 'black',
              width: selected ? 2 : (this.zoom / 8.0)
            }),
            fill: new Fill({
              color: selected ? 'rgba(200,20,20,0.2)' : color
            })
          })

        ]
      }
    },
    getNCCountiesStyle1: function () {
      return feature => {
        return [
          createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 4.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel'
          })
        ]
      }
    },
    getNCCountiesStyle2: function () {
      return feature => {
        return [
          createStyle({
            strokeColor: '#000',
            strokeWidth: (this.zoom / 4.0),
            strokeLineCap: 'round',
            strokeLineJoin: 'bevel'
          })
        ]
      }
    },
    getncwellwiseArsenicMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color2) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color1 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(i * thickness + thickness / 2, 0)
          context.lineTo(i * thickness + thickness / 2, 300)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.arsenic_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 1.0)'
        } else if (data.arsenic_maximum < 4) {
          color = getPattern('rgba(119, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 4 && data.arsenic_maximum < 24) {
          color = getPattern('rgba(143, 52, 235, 1.)')
        } else if (data.arsenic_maximum >= 24 && data.arsenic_maximum < 32) {
          color = getPattern('rgba(165, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 32 && data.arsenic_maximum < 52) {
          color = getPattern('rgba(186, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 52 && data.arsenic_maximum < 62) {
          color = getPattern('rgba(211, 52, 235, 1.0)')
        } else if (data.arsenic_maximum >= 62) {
          color = getPattern('rgba(235, 52, 220, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getncwellwiseCadmiumMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(i * thickness + thickness / 2, 0)
          context.lineTo(i * thickness + thickness / 2, 300)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.cadmium_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 1.0)'
        } else if (data.cadmium_maximum < 5.0) {
          color = getPattern('rgba(235, 89, 52, 1.0)')
        } else if (data.cadmium_maximum >= 5.0 && data.cadmium_maximum < 22.0) {
          color = getPattern('rgba(235, 131, 52, 1.0)')
        } else if (data.cadmium_maximum >= 22.0 && data.cadmium_maximum < 33.0) {
          color = getPattern('rgba(235, 162, 52, 1.0)')
        } else if (data.cadmium_maximum >= 33.0 && data.cadmium_maximum < 44.0) {
          color = getPattern('rgba(235, 192, 52, 1.0)')
        } else if (data.cadmium_maximum >= 44.0 && data.cadmium_maximum < 55.0) {
          color = getPattern('rgba(235, 220, 52, 1.0)')
        } else if (data.cadmium_maximum >= 55.0) {
          color = getPattern('rgba(223, 235, 52, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getncwellwiseLeadMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color1) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color2 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(0, i * thickness + thickness / 2)
          context.lineTo(300, i * thickness + thickness / 2)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }

      return feature => {
        let data = feature.getProperties()
        let color
        if (data.lead_maximum === -999.99) {
          color = 'rgba(50, 110, 219, 1.0)'
        } else if (data.lead_maximum < 11.0) {
          color = getPattern('rgba(196, 200, 207, 1.0)')
        } else if (data.lead_maximum >= 11.0 && data.lead_maximum < 30.0) {
          color = getPattern('rgba(156, 162, 173, 1.0)')
        } else if (data.lead_maximum >= 30.0 && data.lead_maximum < 50.0) {
          color = getPattern('rgba(116, 121, 130, 1.0)')
        } else if (data.lead_maximum >= 50.0 && data.lead_maximum < 80.0) {
          color = getPattern('rgba(79, 82, 89, 1.0)')
        } else if (data.lead_maximum >= 80.0 && data.lead_maximum < 100.0) {
          color = getPattern('rgba(55, 58, 64, 1.0)')
        } else if (data.lead_maximum >= 100.0) {
          color = getPattern('rgba(39, 40, 43, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getncwellwiseMngMaxStyle: function () {
      let canvas = document.createElement('canvas')
      let context = canvas.getContext('2d')
      let pixelRatio = DEVICE_PIXEL_RATIO

      function getPattern (color2) {
        canvas.width = 8 * pixelRatio
        canvas.height = 8 * pixelRatio
        let color1 = 'rgb(0, 0, 0, 0.0)'
        let numberOfStripes = 50
        for (var i = 0; i < numberOfStripes; i++) {
          var thickness = 200 / numberOfStripes
          context.beginPath()
          context.strokeStyle = i % 2 ? color1 : color2
          context.lineWidth = thickness
          context.lineCap = 'round'

          context.moveTo(0, i * thickness + thickness / 2)
          context.lineTo(300, i * thickness + thickness / 2)
          context.stroke()
        }
        return context.createPattern(canvas, 'repeat')
      }
      return feature => {
        let data = feature.getProperties()
        let color
        if (data.manganese_maximum === -999.99) {
          color = 'rgba(91, 95, 99, 1.0)'
        } else if (data.manganese_maximum < 2800.0) {
          color = getPattern('rgba(194, 232, 190, 1.0)')
        } else if (data.manganese_maximum >= 2800.0 && data.manganese_maximum < 5800.0) {
          color = getPattern('rgba(81, 222, 67, 1.0)')
        } else if (data.manganese_maximum >= 5800.0 && data.manganese_maximum < 10800.0) {
          color = getPattern('rgba(25, 128, 11, 1.0)')
        } else if (data.manganese_maximum >= 10800.0 && data.manganese_maximum < 20800.0) {
          color = getPattern('rgba(14, 82, 5, 1.0)')
        } else if (data.manganese_maximum >= 20800.0 && data.manganese_maximum < 40800.0) {
          color = getPattern('rgba(30, 138, 114, 1.0)')
        } else if (data.manganese_maximum >= 40800.0) {
          color = getPattern('rgba(5, 97, 76, 1.0)')
        }
        return [
          new Style({
            stroke: new Stroke({
              color: '#000',
              width: (this.zoom / 8.0),
              lineCap: 'round',
              lineJoin: 'bevel'
            }),
            fill: new Fill({
              color: color
            })
          })
        ]
      }
    },
    getNCWellwiseLayer1ID: function () {
      return 'ncwellwise_layer1'
    },
    getACSCensusLayer1ID: function () {
      return 'acs_census_layer1'
    },
    getEJScreenLayer1ID: function () {
      return 'ejscreen_layer1'
    },
    getCovid19Layer1ID: function () {
      return 'covid19_layer1'
    },
    getNCWellwiseLayer2ID: function () {
      return 'ncwellwise_layer2'
    },
    getACSCensusLayer2ID: function () {
      return 'acs_census_layer2'
    },
    getEJScreenLayer2ID: function () {
      return 'ejscreen_layer2'
    },
    getCovid19Layer2ID: function () {
      return 'covid19_layer2'
    },
    onMapMounted: function (map1) {
      // now ol.Map instance is ready and we can work with it directly
      this.$refs.map1.$map.getControls().extend([
        new Zoom({
          target: 'Zoom1Target'
        }),
        new ScaleLine({
          target: 'Scale1Target'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMap1Target'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'Attribution1Target'
        })
      ])
      this.$refs.map2.$map.getControls().extend([
        /* new Zoom({
          target: 'Zoom2Target'
        }),
        new ScaleLine({
          target: 'Scale2Target'
        }),
        new OverviewMap({
          collapsed: false,
          collapsible: true,
          target: 'OverviewMap2Target'
        }),
        new Attribution({
          collapsed: false,
          collapsible: false,
          target: 'Attribution2Target'
        }) */
      ])
    },
    // base layers
    showBaseLayer1: function () {
      let layer = this.baseLayers1.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      layer = this.baseLayers1.find(layer => layer.name === this.baselayer1)
      if (layer != null) {
        layer.visible = true
      }
    },
    // base layers
    showBaseLayer2: function () {
      let layer = this.baseLayers2.find(layer => layer.visible)
      if (layer != null) {
        layer.visible = false
      }

      layer = this.baseLayers2.find(layer => layer.name === this.baselayer2)
      if (layer != null) {
        layer.visible = true
      }
    },
    showMap1PanelToggleLayer: function () {
      let cntlayer = this.layers1[4]
      if (this.ncCountiesModel1 === 'Selected') {
        cntlayer.visible = true
      } else if (this.ncCountiesModel1 === 'Not Selected') {
        cntlayer.visible = false
      }
    },
    showMap2PanelToggleLayer: function () {
      let cntlayer = this.layers2[4]
      if (this.ncCountiesModel2 === 'Selected') {
        cntlayer.visible = true
      } else if (this.ncCountiesModel2 === 'Not Selected') {
        cntlayer.visible = false
      }
    },
    showMap1PanelRadioLayer: function () {
      let layer = this.layers1.find(layer => layer.visible)

      if (layer != null) {
        layer.visible = false
      }

      var i
      if (this.currentlayer1 === 'ncwellwise_arsenic_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_arsenic_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_arsenic_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_cadmium_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_cadmium_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_cadmium_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_lead_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_lead_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_lead_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_mng_med') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_mng_mean') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'ncwellwise_mng_prcast') {
        layer = this.layers1.find(layer => layer.id === 'ncwellwise_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'percent_below_poverty_level') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'percent_below_poverty_level') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'speak_a_language_other_than_english') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'two_or_more_races') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'asian_alone') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'american_indian_and_alaska_native_alone') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'native_hawaiian_and_other_pacific_islander_alone') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'white_alone') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'black_or_african_american_alone') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'not_hispanic_or_latino') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'hispanic_or_latino_of_any_race') {
        layer = this.layers1.find(layer => layer.id === 'acs_census_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ldpnt_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_dslpm_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_cancr_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_resp_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ptraf_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_pwdis_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_pnpl_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_prmp_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ptsdf_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_ozone_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'd_pm25_2') {
        layer = this.layers1.find(layer => layer.id === 'ejscreen_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'cases') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'cases_per_10000_res') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'cases_per_100000_res') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      } else if (this.currentlayer1 === 'deaths') {
        layer = this.layers1.find(layer => layer.id === 'covid19_layer1')
        for (i = 0; i < this.$refs.layer1Style.length; i++) { this.$refs.layer1Style[i].refresh() }
        // this.$refs.layer1Style.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }
    },
    showMap2PanelRadioLayer: function () {
      let layer = this.layers2.find(layer => layer.visible)

      if (layer != null) {
        layer.visible = false
      }

      var i
      if (this.currentlayer2 === 'ncwellwise_arsenic_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_arsenic_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_arsenic_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_cadmium_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_cadmium_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_cadmium_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_lead_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_lead_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_lead_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_mng_med') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_mng_mean') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'ncwellwise_mng_prcast') {
        layer = this.layers2.find(layer => layer.id === 'ncwellwise_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'percent_below_poverty_level') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'percent_below_poverty_level') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'speak_a_language_other_than_english') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'two_or_more_races') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'asian_alone') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'american_indian_and_alaska_native_alone') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'native_hawaiian_and_other_pacific_islander_alone') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'white_alone') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'black_or_african_american_alone') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'not_hispanic_or_latino') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'hispanic_or_latino_of_any_race') {
        layer = this.layers2.find(layer => layer.id === 'acs_census_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ldpnt_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_dslpm_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_cancr_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_resp_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ptraf_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_pwdis_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_pnpl_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_prmp_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ptsdf_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_ozone_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'd_pm25_2') {
        layer = this.layers2.find(layer => layer.id === 'ejscreen_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'cases') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'cases_per_10000_res') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'cases_per_100000_res') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      } else if (this.currentlayer2 === 'deaths') {
        layer = this.layers2.find(layer => layer.id === 'covid19_layer2')
        for (i = 0; i < this.$refs.layer2Style.length; i++) { this.$refs.layer2Style[i].refresh() }
        // this.$refs.layer2Style.refresh()
      }

      if (layer != null) {
        layer.visible = true
      }
    }
  }
}
</script>

<style lang="scss">
  .ol-control button {
    color: black;
    background-color: rgb(0,128,128);
  }
  .ol-control button:hover {
    text-decoration: none;
    background-color: rgb(0,128,128);
  }
  .ol-control button:focus {
    text-decoration: none;
    background-color: rgb(0,128,128);
  }
  .ol-control button:hover, {
    text-decoration: none;
    background-color: rgba(0,128,128,0.8);
  }
  .ol-control button:focus {
    text-decoration: none;
    background-color: rgba(0,128,128,0.8);
  }
  .ol-scale-line {
    background: rgba(0,128,128,0.8);
  }
  a:hover {
    font-weight:bold;
  }
  .wrapper {
    display: flex;
  }
  .dualmap {
    margin: 0;
    padding: 1px;
    width: 50%;
    height: 100%;
  }
  .view {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
  }
  .feature-popup {
    position: absolute;
    left: -20px;
    bottom: 12px;
    width: 32em;
    max-width: none;
  }
  .feature-popup:after, .feature-popup:before {
    top: 100%;
    border: solid transparent;
    content: ' ';
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
  }
  .feature-popup:after {
    border-top-color: white;
    border-width: 10px;
    left: 48px;
    margin-left: -10px;
  }
  .feature-popup:before {
    border-top-color: #cccccc;
    border-width: 11px;
    left: 48px;
    margin-left: -11px;
  }
  .feature-popup .card-content {
    max-height: 20em;
    overflow: auto;
  }
  .feature-popup .content {
    word-break: break-all;
  }
  .squfill {
    height: 15px;
    width: 15px;
    background-color: rgba(91, 95, 99, 0.65);
    display: inline-block;
  }
  .pbsqufill {
    height: 15px;
    width: 15px;
    background-color: rgba(50, 110, 219, 0.65);
    display: inline-block;
  }
  .assqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 52, 220, 0.65);
    display: inline-block;
  }
  .assqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(186, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(165, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(143, 52, 235, 0.65);
    display: inline-block;
  }
  .assqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(119, 52, 235, 0.65);
    display: inline-block;
  }
  .cdsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 89, 52, 0.65);
    display: inline-block;
  }
  .cdsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 131, 52, 0.65);
    display: inline-block;
  }
  .cdsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 162, 52, 0.65);
    display: inline-block;
  }
  .cdsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 192, 52, 0.65);
    display: inline-block;
  }
  .cdsqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(223, 235, 52, 0.65);
    display: inline-block;
  }
  .pbsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(196, 200, 207, 0.65);
    display: inline-block;
  }
  .pbsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(156, 162, 173, 0.65);
    display: inline-block;
  }
  .pbsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(116, 121, 130, 0.65);
    display: inline-block;
  }
  .pbsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(79, 82, 89, 0.65);
    display: inline-block;
  }
  .pbsqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(39, 40, 43, 0.65);
    display: inline-block;
  }
  .mnsqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(194, 232, 190, 0.65);
    display: inline-block;
  }
  .mnsqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(81, 222, 67, 0.65);
    display: inline-block;
  }
  .mnsqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(25, 128, 11, 0.65);
    display: inline-block;
  }
  .mnsqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(14, 82, 5, 0.65);
    display: inline-block;
  }
  .mnsqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(5, 97, 76, 0.65);
    display: inline-block;
  }
  .acssqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 210, 211, 0.65);
    display: inline-block;
  }
  .acssqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 109, 114, 0.65);
    display: inline-block;
  }
  .acssqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(247, 59, 66, 0.65);
    display: inline-block;
  }
  .acssqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(250, 2, 11, 0.65);
    display: inline-block;
  }
  .acssqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(181, 2, 6, 0.65);
    display: inline-block;
  }
  .acssqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(140, 1, 5, 0.65);
    display: inline-block;
  }
  .heasqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 240, 219, 0.65);
    display: inline-block;
  }
  .heasqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 223, 240, 0.65);
    display: inline-block;
  }
  .heasqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(34, 185, 240, 0.65);
    display: inline-block;
  }
  .heasqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(22, 141, 245, 0.65);
    display: inline-block;
  }
  .heasqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(22, 74, 245, 0.65);
    display: inline-block;
  }
  .heasqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(23, 2, 247, 0.65);
    display: inline-block;
  }
  .ejssqu1 {
    height: 15px;
    width: 15px;
    background-color: rgba(235, 252, 3, 0.65);
    display: inline-block;
  }
  .ejssqu2 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 227, 3, 0.65);
    display: inline-block;
  }
  .ejssqu3 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 186, 3, 0.65);
    display: inline-block;
  }
  .ejssqu4 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 128, 3, 0.65);
    display: inline-block;
  }
  .ejssqu5 {
    height: 15px;
    width: 15px;
    background-color: rgba(252, 82, 3, 0.65);
    display: inline-block;
  }
  .ejssqu6 {
    height: 15px;
    width: 15px;
    background-color: rgba(140, 1, 5, 0.65);
    display: inline-block;
  }
  .q-input {
    height: 4.0em;
  }
  .q-select {
    height: 4.0em;
  }
</style>
