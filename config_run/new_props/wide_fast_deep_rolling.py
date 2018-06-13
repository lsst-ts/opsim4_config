import lsst.pex.config as pexConfig
from lsst.sims.ocs.configuration.proposal import General, GeneralBandFilter, Selection, SelectionList, TimeRange
from lsst.sims.ocs.configuration.proposal import general_prop_reg
__all__ = ["WideFastDeepRolling"]
@pexConfig.registerConfig("WideFastDeepRolling", general_prop_reg, General)
class WideFastDeepRolling(General):
    def setDefaults(self):
        self.name = "WideFastDeepRolling"
        # -------------------------
        # Sky Region specifications
        # -------------------------
        sel1 = Selection()
        sel1.limit_type = "Dec"
        sel1.minimum_limit = -62.5
        sel1.maximum_limit = 2.8
        sel2 = Selection()
        sel2.limit_type = "Dec"
        sel2.minimum_limit = -15.2
        sel2.maximum_limit = 2.8
        sel3 = Selection()
        sel3.limit_type = "Dec"
        sel3.minimum_limit = -35.0
        sel3.maximum_limit = -15.2
        sel4 = Selection()
        sel4.limit_type = "Dec"
        sel4.minimum_limit = -62.5
        sel4.maximum_limit = -35.0
        sel5 = Selection()
        sel5.limit_type = "Dec"
        sel5.minimum_limit = -15.2
        sel5.maximum_limit = 2.8
        sel6 = Selection()
        sel6.limit_type = "Dec"
        sel6.minimum_limit = -35.0
        sel6.maximum_limit = -15.2
        sel7 = Selection()
        sel7.limit_type = "Dec"
        sel7.minimum_limit = -62.5
        sel7.maximum_limit = -35.0
        sel8 = Selection()
        sel8.limit_type = "Dec"
        sel8.minimum_limit = -15.2
        sel8.maximum_limit = 2.8
        sel9 = Selection()
        sel9.limit_type = "Dec"
        sel9.minimum_limit = -35.0
        sel9.maximum_limit = -15.2
        sel10 = Selection()
        sel10.limit_type = "Dec"
        sel10.minimum_limit = -62.5
        sel10.maximum_limit = -35.0
        sel11 = Selection()
        sel11.limit_type = "Dec"
        sel11.minimum_limit = -62.5
        sel11.maximum_limit = 2.8
        self.sky_region.selections = {1: sel1,
                                      2: sel2,
                                      3: sel3,
                                      4: sel4,
                                      5: sel5,
                                      6: sel6,
                                      7: sel7,
                                      8: sel8,
                                      9: sel9,
                                      10: sel10,
                                      11: sel11}
        time_range1 = TimeRange()
        time_range1.start = 1
        time_range1.end = 365
        time_range2 = TimeRange()
        time_range2.start = 366
        time_range2.end = 690
        time_range3 = TimeRange()
        time_range3.start = 691
        time_range3.end = 1015
        time_range4 = TimeRange()
        time_range4.start = 1016
        time_range4.end = 1340
        time_range5 = TimeRange()
        time_range5.start = 1341
        time_range5.end = 1665
        time_range6 = TimeRange()
        time_range6.start = 1666
        time_range6.end = 1990
        time_range7 = TimeRange()
        time_range7.start = 1991
        time_range7.end = 2315
        time_range8 = TimeRange()
        time_range8.start = 2316
        time_range8.end = 2639
        time_range9 = TimeRange()
        time_range9.start = 2640
        time_range9.end = 2963
        time_range10 = TimeRange()
        time_range10.start = 2964
        time_range10.end = 3287
        time_range11 = TimeRange()
        time_range11.start = 3288
        time_range11.end = 3650
        self.sky_region.time_ranges = {1: time_range1,
                                       2: time_range2,
                                       3: time_range3,
                                       4: time_range4,
                                       5: time_range5,
                                       6: time_range6,
                                       7: time_range7,
                                       8: time_range8,
                                       9: time_range9,
                                       10: time_range10,
                                       11: time_range11}
        sel_map1 = SelectionList()
        sel_map1.indexes = [1]
        sel_map2 = SelectionList()
        sel_map2.indexes = [2]
        sel_map3 = SelectionList()
        sel_map3.indexes = [3]
        sel_map4 = SelectionList()
        sel_map4.indexes = [4]
        sel_map5 = SelectionList()
        sel_map5.indexes = [5]
        sel_map6 = SelectionList()
        sel_map6.indexes = [6]
        sel_map7 = SelectionList()
        sel_map7.indexes = [7]
        sel_map8 = SelectionList()
        sel_map8.indexes = [8]
        sel_map9 = SelectionList()
        sel_map9.indexes = [9]
        sel_map10 = SelectionList()
        sel_map10.indexes = [10]
        sel_map11 = SelectionList()
        sel_map11.indexes = [11]
        self.sky_region.selection_mapping = {1: sel_map1,
                                             2: sel_map2,
                                             3: sel_map3,
                                             4: sel_map4,
                                             5: sel_map5,
                                             6: sel_map6,
                                             7: sel_map7,
                                             8: sel_map8,
                                             9: sel_map9,
                                             10: sel_map10,
                                             11: sel_map11}

        # ----------------------------
        # Sky Exclusion specifications
        # ----------------------------
        self.sky_exclusion.dec_window = 90.0
        excl0 = Selection()
        excl0.limit_type = "GP"
        excl0.minimum_limit = 0.0
        excl0.maximum_limit = 10.0
        excl0.bounds_limit = 90.0
        self.sky_exclusion.selections = {0: excl0}
        # ---------------------------------
        # Sky Nightly Bounds specifications
        # ---------------------------------
        self.sky_nightly_bounds.twilight_boundary = -12.0
        self.sky_nightly_bounds.delta_lst = 60.0
        # ------------------------------
        # Sky Constraints specifications
        # ------------------------------
        self.sky_constraints.max_airmass = 1.5
        self.sky_constraints.max_cloud = 0.7
        # ----------------------
        # Scheduling information
        # ----------------------
        self.scheduling.max_num_targets = 500
        self.scheduling.accept_serendipity = False
        self.scheduling.accept_consecutive_visits = False
        self.scheduling.restrict_grouped_visits = True
        self.scheduling.time_interval = 1800
        self.scheduling.time_window_start = .5
        self.scheduling.time_window_max = 1.0
        self.scheduling.time_window_end = 2.0
        self.scheduling.time_weight = 1.0
        self.sky_constraints.max_cloud = 0.7
        # ----------------
        # HA and X bonuses
        # ----------------
        self.scheduling.airmass_bonus=0.0
        self.scheduling.hour_angle_bonus=0.3
        self.scheduling.hour_angle_max=3.0
        # --------------------------
        # Band Filter specifications
        # --------------------------
        u_filter = GeneralBandFilter()
        u_filter.name = 'u'
        u_filter.num_visits = 75
        u_filter.num_grouped_visits = 1
        u_filter.bright_limit = 21.3
        u_filter.dark_limit = 30.0
        u_filter.max_seeing = 1.5
        u_filter.exposures = [15.0, 15.0]
        g_filter = GeneralBandFilter()
        g_filter.name = 'g'
        g_filter.num_visits = 105
        g_filter.num_grouped_visits = 2
        g_filter.bright_limit = 21.0
        g_filter.dark_limit = 30.0
        g_filter.max_seeing = 1.5
        g_filter.exposures = [15.0, 15.0]
        r_filter = GeneralBandFilter()
        r_filter.name = 'r'
        r_filter.num_visits = 240
        r_filter.num_grouped_visits = 2
        r_filter.bright_limit = 20.25
        r_filter.dark_limit = 30.0
        r_filter.max_seeing = 1.5
        r_filter.exposures = [15.0, 15.0]
        i_filter = GeneralBandFilter()
        i_filter.name = 'i'
        i_filter.num_visits = 240
        i_filter.num_grouped_visits = 2
        i_filter.bright_limit = 19.5
        i_filter.dark_limit = 30.0
        i_filter.max_seeing = 1.5
        i_filter.exposures = [15.0, 15.0]
        z_filter = GeneralBandFilter()
        z_filter.name = 'z'
        z_filter.num_visits = 210
        z_filter.num_grouped_visits = 2
        z_filter.bright_limit = 17.0
        z_filter.dark_limit = 21.0
        z_filter.max_seeing = 1.5
        z_filter.exposures = [15.0, 15.0]
        y_filter = GeneralBandFilter()
        y_filter.name = 'y'
        y_filter.num_visits = 210
        y_filter.num_grouped_visits = 1
        y_filter.bright_limit = 16.5
        y_filter.dark_limit = 21.0
        y_filter.max_seeing = 1.5
        y_filter.exposures = [15.0, 15.0]
        self.filters = {u_filter.name: u_filter,
                        g_filter.name: g_filter,
                        r_filter.name: r_filter,
                        i_filter.name: i_filter,
                        z_filter.name: z_filter,
                        y_filter.name: y_filter}
