import solutions

class Tests:

    def test_is_sweltering(self, monkeypatch):
        # test with a super hot temperature
        monkeypatch.setattr("builtins.input", lambda x: '121')
        result = solutions.is_sweltering()
        assert result == True

        # test with the threshold temperature
        monkeypatch.setattr("builtins.input", lambda x: '90')
        result = solutions.is_sweltering()
        assert result == False

        # test with a cold temperature
        monkeypatch.setattr("builtins.input", lambda x: '52')
        result = solutions.is_sweltering()
        assert result == False

    def test_is_warm(self, capsys, monkeypatch):
        # test with a super hot temperature
        monkeypatch.setattr("builtins.input", lambda x: '121')
        result = solutions.is_warm()
        assert result == False

        # test with the threshold temperature
        monkeypatch.setattr("builtins.input", lambda x: '87')
        result = solutions.is_warm()
        assert result == True

        # test with the threshold temperature
        monkeypatch.setattr("builtins.input", lambda x: '75')
        result = solutions.is_warm()
        assert result == True

        # test with a cold temperature
        monkeypatch.setattr("builtins.input", lambda x: '52')
        result = solutions.is_warm()
        assert result == False

    def test_is_humid(self, capsys, monkeypatch):
        # test with a 'yes'
        monkeypatch.setattr("builtins.input", lambda x: 'yes')
        result = solutions.is_humid()
        assert result == True

        # test with a 'no'
        monkeypatch.setattr("builtins.input", lambda x: 'no')
        result = solutions.is_humid()
        assert result == False

    def test_is_inclement(self, capsys, monkeypatch):
        # test with 'rain'
        monkeypatch.setattr("builtins.input", lambda x: 'rain')
        result = solutions.is_inclement()
        assert result == True

        # test with 'snow'
        monkeypatch.setattr("builtins.input", lambda x: 'snow')
        result = solutions.is_inclement()
        assert result == True

        # test with 'sleet'
        monkeypatch.setattr("builtins.input", lambda x: 'sleet')
        result = solutions.is_inclement()
        assert result == True

        # test with something else
        monkeypatch.setattr("builtins.input", lambda x: 'foo')
        result = solutions.is_inclement()
        assert result == False

        # test with something else
        monkeypatch.setattr("builtins.input", lambda x: 'bar')
        result = solutions.is_inclement()
        assert result == False

    def test_is_typical_new_york_summer(self, capsys, monkeypatch):
        # test with a hot temperature and humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        result = solutions.is_typical_new_york_summer()
        assert result == True

        # test with a hot temperature but no humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        result = solutions.is_typical_new_york_summer()
        assert result == False

        # test with a cool temperature and humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        result = solutions.is_typical_new_york_summer()
        assert result == False

        # test with a cool temperature and no humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        result = solutions.is_typical_new_york_summer()
        assert result == False

    def test_is_cool_and_nice(self, capsys, monkeypatch):
        # test with a hot temperature and humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with a hot temperature but no humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: True)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with a cool temperature and humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: True)
        result = solutions.is_cool_and_nice()
        assert result == False

        # test with a cool temperature and no humidity
        monkeypatch.setattr("solutions.is_sweltering", lambda: False)
        monkeypatch.setattr("solutions.is_humid", lambda: False)
        result = solutions.is_cool_and_nice()
        assert result == True
