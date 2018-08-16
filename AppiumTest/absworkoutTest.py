import subprocess
import unittest
from time import sleep
from appium import webdriver


class AbsWorkoutTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.1'
        desired_caps['deviceName'] = '03083025d0250909'
        desired_caps['appPackage'] = 'abs.workout.fitness.tabata.hiit.stomach'
        desired_caps['appActivity'] = 'cootek.sevenmins.sport.WelcomeActivityAlias'
        desired_caps['newCommandTimeout'] = 120
        desired_caps['noReset'] = True
        desired_caps['printPageSourceOnFindFailure'] = True
        desired_caps['unicodeKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(10)

    def tearDown(self):
        self.driver.quit()

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUpToCla(self, t=1000, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUpToTab(self, t=100, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeUpSlow(self, t=1000, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    # adb command
    def sh(self, command):
        with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as f:
            print(f.stdout.read())

    # 切换tap页
    def switch_tap(self, tap_num):
        ll_tap = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/ll_tap")
        ll_tap[tap_num].click()
        sleep(2)

    # 获取bug截图
    def get_bug_screenshot(self, loop_num, class_name, count):
        if 7 <= loop_num <= 13:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/' +
                                               'bug/stage2' + 'index' + str(count + 1) + '.png')
        elif 14 <= loop_num <= 20:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/' +
                                               'bug/stage3' + 'index' + str(count + 1) + '.png')
        elif 21 <= loop_num <= 27:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/' +
                                               'bug/stage4' + 'index' + str(count + 1) + '.png')
        else:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/' +
                                               'bug/stage1' + 'index' + str(count + 1) + '.png')

    # 获取课程最后动作的截图
    def get_last_action_screenshot(self, loop_num, class_name, exercise_name, last_num):
        if 7 <= loop_num <= 13:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage2/'
                                               + str(last_num) + exercise_name.text + '.png')
        elif 14 <= loop_num <= 20:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage3/'
                                               + str(last_num) + exercise_name.text + '.png')
        elif 21 <= loop_num <= 27:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage4/'
                                               + str(last_num) + exercise_name.text + '.png')
        else:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage1/'
                                               + str(last_num) + exercise_name.text + '.png')

    # 获取课程动作截图
    def get_action_screenshot(self, loop_num, class_name, exercise_name, count):
        if 7 <= loop_num <= 13:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage2/'
                                               + str(count + 1) + exercise_name.text + '.png')
        elif 14 <= loop_num <= 20:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage3/'
                                               + str(count + 1) + exercise_name.text + '.png')
        elif 21 <= loop_num <= 27:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage4/'
                                               + str(count + 1) + exercise_name.text + '.png')
        else:
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/' + class_name + '/stage1/'
                                               + str(count + 1) + exercise_name.text + '.png')

    # 课程学习-课程视频页-进入课程classic
    def enter_class_video_classic(self):
        self.swipeUpToCla()
        try:
            enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            enter_classic.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/enter_classic_error.png')
            pass
        sleep(2)
        try:
            button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            button_go.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_go_error.png')
            pass
        sleep(2)
        try:
            button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
            button_go2.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_go2_error.png')
            pass
        sleep(2)

    # 遍历课程classic
    def test_class_classic(self):
        self.swipeUpToCla()
        enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_classic.click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "CLASSIC", "进入classic课程错误")
        loop_num = 0
        while loop_num < 28:
            # noinspection PyBroadException
            try:
                button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
                button_go.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/classic/bug/button_go_error.png')
                pass
            sleep(2)
            try:
                button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
                button_go2.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/classic/bug/button_go2_error.png')
                pass
            sleep(2)
            count = 0
            while count < 13:
                # noinspection PyBroadException
                try:
                    global exercise_name
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    self.get_action_screenshot(loop_num, 'classic', exercise_name, count)
                except:
                    self.get_bug_screenshot(loop_num, 'classic', count)
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            self.get_last_action_screenshot(loop_num, 'classic', exercise_name, 14)
            sleep(40)
            try:
                button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
                button_cancel.click()
            except:
                pass
            sleep(2)
            self.sh('adb shell input keyevent 4')
            sleep(2)
            loop_num = loop_num + 1

    # 遍历课程hiit
    def test_class_hiit(self):
        self.swipeUp()
        enter_hiit = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_hiit[1].click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "HIIT", "进入hiit课程错误")
        loop_num = 0
        while loop_num < 28:
            # noinspection PyBroadException
            try:
                button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
                button_go.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/hiit/bug/button_go_error.png')
                pass
            sleep(2)
            try:
                button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
                button_go2.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/hiit/bug/button_go2_error.png')
                pass
            sleep(2)
            count = 0
            while count < 13:
                # noinspection PyBroadException
                try:
                    global exercise_name
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    self.get_action_screenshot(loop_num, 'hiit', exercise_name, count)
                except:
                    self.get_bug_screenshot(loop_num, 'hiit', count)
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            self.get_last_action_screenshot(loop_num, 'hiit', exercise_name, 14)
            sleep(40)
            # noinspection PyBroadException
            try:
                button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
                button_cancel.click()
            except:
                pass
            sleep(2)
            self.sh('adb shell input keyevent 4')
            sleep(2)
            loop_num = loop_num + 1

    # 遍历课程tabata
    def test_class_tabata(self):
        self.swipeUpToTab()
        enter_tabata = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
        enter_tabata[1].click()
        sleep(2)
        title_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/title_tv")
        self.assertEqual(title_text.text, "TABATA", "进入tabata课程错误")
        loop_num = 0
        while loop_num < 28:
            # noinspection PyBroadException
            try:
                button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
                button_go.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/tabata/bug/button_go_error.png')
                pass
            sleep(2)
            try:
                button_go2 = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/go_container")
                button_go2.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/tabata/bug/button_go2_error.png')
                pass
            sleep(2)
            count = 0
            while count < 7:
                # noinspection PyBroadException
                try:
                    global exercise_name
                    exercise_name = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                                   "exercise_name")
                    self.get_action_screenshot(loop_num, 'tabata', exercise_name, count)
                except:
                    self.get_bug_screenshot(loop_num, 'tabata', count)
                    button_ok = self.driver.find_element_by_id("android:id/button1")
                    button_ok.click()
                    sleep(1)
                    self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/tabata/bug/'
                                                       + 'num' + str(loop_num + 1) + 'index' + str(count + 1) + '2.png')
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
                sleep(2)
                count = count + 1
            self.get_last_action_screenshot(loop_num, 'tabata', exercise_name, 8)
            sleep(40)
            # noinspection PyBroadException
            try:
                button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
                button_cancel.click()
            except:
                pass
            sleep(2)
            self.sh('adb shell input keyevent 4')
            sleep(2)
            loop_num = loop_num + 1

    # 课程学习-课程UI展示 --- 已废弃
    # def test_class_ui_classic(self):
    #     self.swipeUpToCla()
    #     enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     enter_classic.click()
    #     sleep(2)
    #     button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
    #     button_go.click()
    #     sleep(2)
    #     # shoulders
    #     sleep(2)
    #     Shoulders = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Shoulders Stretch with Rotation")')
    #     Shoulders.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/shoulders.png')
    #     self.sh('adb shell input keyevent 4')
    #     # jump left
    #     sleep(2)
    #     jump = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Jump Left and Right")')
    #     jump.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/jump.png')
    #     self.sh('adb shell input keyevent 4')
    #     # reverse
    #     sleep(2)
    #     reverse = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Reverse Crunches")')
    #     reverse.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/reverse.png')
    #     self.sh('adb shell input keyevent 4')
    #     # plank
    #     sleep(2)
    #     plank = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Plank")')
    #     plank.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/plank.png')
    #     self.sh('adb shell input keyevent 4')
    #     # cat-cow
    #     sleep(2)
    #     cat = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Cat-Cow Stretch")')
    #     cat.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/cat.png')
    #     self.sh('adb shell input keyevent 4')
    #     sleep(2)
    #     # dead bug
    #     self.swipeUpSlow()
    #     sleep(2)
    #     dead_bug = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Dead Bug")')
    #     dead_bug.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/dead_bug.png')
    #     self.sh('adb shell input keyevent 4')
    #     # jumping jacks
    #     sleep(2)
    #     jumping_jacks = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Jumping Jacks")')
    #     jumping_jacks.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/jumping_jacks.png')
    #     self.sh('adb shell input keyevent 4')
    #     # plank
    #     sleep(2)
    #     plank_2 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Plank")')
    #     plank_2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/plant_2.png')
    #     self.sh('adb shell input keyevent 4')
    #     #########
    #     # dead bug
    #     sleep(2)
    #     self.swipeUpSlow()
    #     sleep(2)
    #     dead_bug_2 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Dead Bug")')
    #     dead_bug_2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/dead_bug_2.png')
    #     self.sh('adb shell input keyevent 4')
    #     # jumping jacks
    #     sleep(2)
    #     jumping_jacks_2 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Jumping Jacks")')
    #     jumping_jacks_2.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/jumping_jacks_2.png')
    #     self.sh('adb shell input keyevent 4')
    #     # plank
    #     sleep(2)
    #     plank_3 = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Plank")')
    #     plank_3.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/plant_3.png')
    #     self.sh('adb shell input keyevent 4')
    #     # calf stretch left
    #     sleep(2)
    #     calf_left = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Calf Stretch Left")')
    #     calf_left.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/calf_left.png')
    #     self.sh('adb shell input keyevent 4')
    #     # calf stretch right
    #     sleep(2)
    #     calf_right = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Calf Stretch Right")')
    #     calf_right.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/calf_right.png')
    #     self.sh('adb shell input keyevent 4')
    #     ###
    #     sleep(2)
    #     self.swipeUp()
    #     sleep(2)
    #     back_stretch = self.driver.find_element_by_android_uiautomator(
    #         'new UiSelector().text("Back Stretch")')
    #     back_stretch.click()
    #     sleep(2)
    #     self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/classic/back_stretch.png')

    # 课程学习-课程列表页-点击"Go"
    def test_class_list_classic_go(self):
        self.enter_class_video_classic()
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/list/go.png')

    # 课程学习-课程列表页-点击动作预览
    def test_class_list_classic_preview(self):
        self.swipeUpToCla()
        try:
            enter_classic = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            enter_classic.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/enter_classic_error.png')
            pass
        sleep(2)
        try:
            button_go = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_start")
            button_go.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_go_error.png')
            pass
        sleep(2)
        try:
            Shoulders = self.driver.find_element_by_android_uiautomator(
                'new UiSelector().text("Shoulders Stretch with Rotation")')
            Shoulders.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/preview_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/list/preview.png')

    # 课程学习-课程视频页-点击底部前后箭头
    def test_class_video_arrows(self):
        self.enter_class_video_classic()
        try:
            button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
            button_next.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_next_error.png')
            pass
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/arrows_two.png')
        try:
            button_back = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/turn_back")
            button_back.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_back_error.png')
            pass
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/arrows_one.png')

    # 课程学习-课程视频页-点击暂停按钮
    def test_class_video_pause(self):
        self.enter_class_video_classic()
        try:
            pause = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/exercise_progress")
            pause.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/pause_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/pause.png')

    # 课程学习-课程视频页-底部音符按钮
    def test_class_video_bgm(self):
        self.enter_class_video_classic()
        try:
            global bgm
            bgm = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/bgm_play_image")
            bgm.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/bgm_error.png')
            pass
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/bgm_off.png')
        bgm.click()
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/bgm_on.png')

    # 课程学习-课程视频页-扬声器按钮
    def test_class_video_sound(self):
        self.enter_class_video_classic()
        try:
            global sound
            sound = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/sound_play_image")
            sound.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/sound_error.png')
            pass
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/sound_off.png')
        sound.click()
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/sound_on.png')

    # 课程学习-课程视频页-点击系统返回键/页面返回键
    def test_class_video_close(self):
        self.enter_class_video_classic()
        try:
            button_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_close")
            button_close.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_close_error.png')
            pass
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/video/close.png')

    # 课程学习-动作暂停页
    def test_class_pause(self):
        self.test_class_video_pause()
        try:
            button_resume = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnResume")
            button_resume.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_resume_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/pause/resume.png')

    # 课程学习-退出运动弹框-关闭
    def test_class_exit_close(self):
        self.test_class_video_close()
        try:
            button_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_close")
            button_close.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_exit_close_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/exit/close.png')

    # 课程学习-退出运动弹框-退出运动
    def test_class_exit_quit(self):
        self.test_class_video_close()
        try:
            button_quit = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnQuit")
            button_quit.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_quit_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/exit/quit.png')

    # 课程学习-退出运动弹框-休息一会儿
    def test_class_exit_snooze(self):
        self.test_class_video_close()
        try:
            button_snooze = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnSnooze")
            button_snooze.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_snooze_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/exit/snooze.png')

    # 课程学习-运动完成页
    def test_class_done(self):
        self.enter_class_video_classic()
        count = 0
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/done/' + str(count) + '.png')
        while count < 13:
            try:
                button_next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_next")
                button_next.click()
            except:
                self.driver.get_screenshot_as_file(
                    '/Users/a140/Desktop/screenshot_absworkout/class/bug/done_button_next.png')
                pass
            sleep(2)
            count = count + 1
            self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/done/' + str(count) + '.png')
        sleep(40)

    # 课程学习-运动完成页-添加/修改体重
    def test_class_done_weight(self):
        self.test_class_done()
        try:
            button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
            button_cancel.click()
        except:
            pass
        try:
            current_weight = self.driver.find_element_by_id(
                "abs.workout.fitness.tabata.hiit.stomach:id/current_weight_tv")
            current_weight.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/current_weight_error.png')
            pass
        try:
            edit_weight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/edit_weight")
            edit_weight.clear()
            edit_weight.send_keys("70")
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/edit_weight_error.png')
            pass
        try:
            edit_height = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/edit_height")
            edit_height.clear()
            edit_height.send_keys("180")
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/edit_height_error.png')
            pass
        try:
            button_save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnSave")
            button_save.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/button_save_error.png')
            pass
        sleep(2)
        self.sh('adb shell input keyevent 4')
        sleep(2)
        self.sh('adb shell input keyevent 4')
        self.switch_tap(1)
        current_weight = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/currentWeight")
        current_height = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/currentHeight")
        try:
            self.assertIn('70', current_weight.text, '体重添加修改失败！')
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/weight_error.png')
        try:
            self.assertIn('180', current_height.text, '身高添加修改失败！')
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/height_error.png')

    # 课程学习-运动完成页-再来一次
    def test_class_done_again(self):
        self.test_class_done()
        try:
            button_cancel = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_cancel")
            button_cancel.click()
        except:
            pass
        try:
            again = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Once again")')
            again.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/done_again_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/class/done/again.png')

    # 课程学习-运动完成页-分享
    def test_class_done_share(self):
        pass

    # 分享
    def test_share(self):
        pass

    # 记录页
    def test_track(self):
        pass

    # 成就页
    def test_achievement(self):
        pass

    # 初次打开app
    def test_enter_choice_item(self):
        try:
            item_button = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/item_button")
            item_button[2].click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/enter_item_button_error.png')
            pass
        sleep(2)
        try:
            next = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/next")
            next.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/enter_next_error.png')
            pass
        sleep(2)
        try:
            start = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btn_ok")
            start.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/class/bug/enter_start_error.png')
            pass

    # 设置页-去除广告
    def test_setting_ad(self):
        try:
            setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
            setting.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/enter_setting_error.png')
            pass
        try:
            remove_ad = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                       "setting_item_premium_entry")
            remove_ad.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/setting_remove_ad_error.png')
            pass
        sleep(1)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/after_click_remove_ad.png')
        remove_ad_close = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/iv_close")
        remove_ad_close.click()

    # 设置页-添加提醒
    def test_setting_reminder_add(self):
        try:
            setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
            setting.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/enter_setting_error.png')
            pass
        try:
            add_reminder = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/add_tag")
            add_reminder.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/setting_add_reminder_error.png')
            pass
        try:
            reminder_label = self.driver.find_element_by_id(
                "abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
            reminder_label.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/setting_reminder_label_error.png')
            pass
        try:
            label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
            label_list[2].click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/setting_label_list_error.png')
            pass
        try:
            repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
            repeat_day[0].click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/setting_repeat_day_error.png')
            pass
        try:
            save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
            save.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/setting_save_error.png')
            pass
        sleep(2)
        try:
            global reminder_text
            reminder_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/reminder_text_error.png')
            pass
        try:
            self.assertEqual(reminder_text.text, 'TABATA, Mon Tue Wed Thu Fri Sat', '添加提醒错误')
        except Exception as msg:
            print(msg)
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/reminder_add_error.png')
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/reminder_add.png')

    # 设置页-关闭提醒
    def test_setting_reminder_off(self):
        try:
            setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
            setting.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/enter_setting_error.png')
            pass
        try:
            switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
            switch_reminder[0].click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/switch_reminder_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/reminder_off.png')

    # 设置页-打开提醒
    def test_setting_reminder_on(self):
        try:
            setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
            setting.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/enter_setting_error.png')
            pass
        try:
            switch_reminder = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/switch_btn")
            switch_reminder[0].click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/switch_reminder_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/reminder_on.png')

    # 设置页-删除提醒
    def test_setting_reminder_delete(self):
        try:
            setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
            setting.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/enter_setting_error.png')
            pass
        try:
            reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
            reminder_list[0].click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/reminder_list_error.png')
            pass
        sleep(2)
        self.swipeUp()
        try:
            button_delete = self.driver.find_element_by_id(
                "abs.workout.fitness.tabata.hiit.stomach:id/reminder_delete_btn")
            button_delete.click()
        except:
            self.driver.get_screenshot_as_file(
                '/Users/a140/Desktop/screenshot_absworkout/setting/bug/button_delete_error.png')
            pass
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/delete_done.png')

    # 设置页-修改提醒
    def test_setting_reminder_update(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        reminder_list = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        reminder_list[0].click()
        reminder_label = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_program")
        reminder_label.click()
        label_list = self.driver.find_elements_by_class_name("android.widget.LinearLayout")
        label_list[1].click()
        reminder_time = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/reminder_time")
        reminder_time.click()
        sleep(1)
        button_ok = self.driver.find_element_by_id("android:id/button1")
        button_ok.click()
        self.swipeUp()
        repeat_day = self.driver.find_elements_by_id("abs.workout.fitness.tabata.hiit.stomach:id/day_check")
        repeat_day[3].click()
        repeat_day[4].click()
        repeat_day[5].click()
        repeat_day[6].click()
        save = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/btnRight")
        save.click()
        sleep(2)
        reminder_update_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/program_info")
        self.assertEqual(reminder_update_text.text, 'HIIT, Mon Tue ', '修改提醒错误')
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/reminder_update.png')

    # 设置页-反馈意见
    def test_setting_feedback(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        feedback = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/feedback")
        feedback.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/feedback.png')

    # 设置页-分享应用
    def test_setting_share(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        share = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/share")
        share.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/share.png')

    # 设置页-隐私政策
    def test_setting_privacy(self):
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        privacy = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/"
                                                 "view_setting_item_privacy_policy")
        privacy.click()
        sleep(2)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/privacy.png')

    # 设置页-版本号
    def test_setting_version(self):
        version = "1.6.1"
        setting = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/toolbar_setting")
        setting.click()
        self.swipeUp()
        sleep(2)
        version_text = self.driver.find_element_by_id("abs.workout.fitness.tabata.hiit.stomach:id/version")
        self.assertEqual(version_text.text, version)
        self.driver.get_screenshot_as_file('/Users/a140/Desktop/screenshot_absworkout/setting/version.png')

    # 课程学习
    def suite_class(self):
        suite = unittest.TestSuite()
        suite.addTest(AbsWorkoutTest('test_class_list_classic_go'))
        suite.addTest(AbsWorkoutTest('test_class_list_classic_preview'))
        suite.addTest(AbsWorkoutTest('test_class_video_arrows'))
        suite.addTest(AbsWorkoutTest('test_class_video_pause'))
        suite.addTest(AbsWorkoutTest('test_class_video_bgm'))
        suite.addTest(AbsWorkoutTest('test_class_video_sound'))
        suite.addTest(AbsWorkoutTest('test_class_video_close'))
        suite.addTest(AbsWorkoutTest('test_class_pause'))
        suite.addTest(AbsWorkoutTest('test_class_exit_close'))
        suite.addTest(AbsWorkoutTest('test_class_exit_quit'))
        suite.addTest(AbsWorkoutTest('test_class_exit_snooze'))
        suite.addTest(AbsWorkoutTest('test_class_done'))
        suite.addTest(AbsWorkoutTest('test_class_done_weight'))
        suite.addTest(AbsWorkoutTest('test_class_done_again'))
        suite.addTest(AbsWorkoutTest('test_class_done_share'))
        return suite

    # 设置页
    def suite_setting(self):
        suite = unittest.TestSuite()
        suite.addTest(AbsWorkoutTest('test_enter_choice_item'))
        suite.addTest(AbsWorkoutTest('test_setting_ad'))
        suite.addTest(AbsWorkoutTest('test_setting_reminder_add'))
        suite.addTest(AbsWorkoutTest('test_setting_reminder_off'))
        suite.addTest(AbsWorkoutTest('test_setting_reminder_on'))
        suite.addTest(AbsWorkoutTest('test_setting_reminder_delete'))
        suite.addTest(AbsWorkoutTest('test_setting_reminder_update'))
        suite.addTest(AbsWorkoutTest('test_setting_feedback'))
        suite.addTest(AbsWorkoutTest('test_setting_share'))
        suite.addTest(AbsWorkoutTest('test_setting_privacy'))
        suite.addTest(AbsWorkoutTest('test_setting_version'))
        return suite

    # 遍历所有课程
    def suite_class_all(self):
        suite = unittest.TestSuite()
        suite.addTest(AbsWorkoutTest('test_class_classic'))
        suite.addTest(AbsWorkoutTest('test_class_hiit'))
        suite.addTest(AbsWorkoutTest('test_class_tabata'))
        return suite

    if __name__ == '__main__':
        runner = unittest.TextTestRunner(failfast=True)
        runner.run(suite_class_all())


# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(AbsWorkoutTest)
#     unittest.TextTestRunner(verbosity=2).run(suite)