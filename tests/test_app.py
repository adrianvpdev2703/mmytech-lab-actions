import unittest
from src.app import check_host_status, calculate_allocated_resources


class TestApp(unittest.TestCase):

    def test_check_host_status_valid(self):
        result = check_host_status("srv-ansible-01")
        self.assertEqual(result["host"], "srv-ansible-01")
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["status"], "active")

    def test_check_host_status_invalid(self):
        with self.assertRaises(ValueError):
            check_host_status("")

    def test_calculate_allocated_resources_success(self):
        res = calculate_allocated_resources(4, 16)
        self.assertEqual(res["cores"], 4)
        self.assertEqual(res["ram_gb"], 16)
        self.assertTrue(res["ready_to_deploy"])

    def test_calculate_allocated_resources_error(self):
        with self.assertRaises(ValueError):
            calculate_allocated_resources(0, 8)


if __name__ == "__main__":
    unittest.main()
