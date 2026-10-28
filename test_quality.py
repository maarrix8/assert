from quality import classify_score, normalize_status, apply_result, summarize, run_tests
def test_score():
    assert classify_score(1) == "fail", f"Вход 1 должен дать fail, получено {classify_score(1)}"
    assert classify_score(0) == "fail", f"Вход 0 должен дать fail, получено {classify_score(0)}"
    assert classify_score(59) == "fail", f"Вход 59 должен дать fail, получено {classify_score(59)}"
    assert classify_score(60) == "pass", f"Вход 60 должен дать pass, получено {classify_score(60)}"
    assert classify_score(61) == "pass", f"Вход 61 должен дать pass, получено {classify_score(61)}"
    assert classify_score(100) == "pass", f"Вход 100 должен дать pass, получено {classify_score(100)}"
    assert classify_score(101) is None, f"Вход 101 должен дать None, получено {classify_score(101)}"

def test_status():
    assert normalize_status("pass") == "pass"
    assert normalize_status("FAIL ") == "fail"
    assert normalize_status(" Pending ") == "pending"
    assert normalize_status("") is None
    assert normalize_status("   ") is None
    assert normalize_status("done") is None


def test_apply():
    record1 = {"id": 7, "title": "Вход ЕКЕВ", "status": "pending"}
    before1 = record1.copy()
    res1 = apply_result(record1, " PASS ")
    assert res1 is True
    assert record1["status"] == "pass"
    assert record1["id"] == before1["id"]
    assert record1["title"] == before1["title"]

    record2 = {"id": 7, "title": "Вход ЕКЕВ", "status": "pending"}
    before2 = record2.copy()
    res2 = apply_result(record2, "done")
    assert res2 is False
    assert record2 == before2
    record3 = {"id": 7, "title": "Вход ЕКЕВ", "status": "pass"}
    before3 = record3.copy()
    res3 = apply_result(record3, "pass")
    assert res3 is True
    assert record3 == before3

def test_summary():
    records = [
        {"id": 1, "title": "Вход ЕКЕВ", "status": "pass"},
        {"id": 4, "title": "Профиль", "status": "fail"},
        {"id": 7, "title": "Расписание", "status": "pass"},
        {"id": 9, "title": "Выход", "status": "pending"}
    ]
    records_snapshot = [r.copy() for r in records]
    summary_result = summarize(records)
    assert summary_result == {"total": 4, "pending": 1, "pass": 2, "fail": 1}
    assert records == records_snapshot
    assert summarize([]) == {"total": 0, "pending": 0, "pass": 0, "fail": 0}
    single_fail = [{"id": 10, "title": "Тест", "status": "fail"}]
    assert summarize(single_fail) == {"total": 1, "pending": 0, "pass": 0, "fail": 1}

def test_runner_mock():
    def mock_pass():
        assert True
    def mock_fail():
        assert False, "Учебный отказ"
        
    res = run_tests([mock_pass, mock_fail])
    assert res["total"] == 2
    assert res["passed"] == 1
    assert res["failed"] == 1

def main():
    tests = [test_score, test_status, test_apply, test_summary, test_runner_mock]
    print("Запуск автотестов...")
    result = run_tests(tests)
    print(f"Итог: Всего: {result['total']}, Успешно: {result['passed']}, Ошибок: {result['failed']}")

if __name__ == "__main__":
    main()