from dummy_api_plugin import DummyApiPlugin


def main():
    # A valid instance of the DummyApiPlugin
    plugin = DummyApiPlugin("emilys", "emilyspass")
    plugin.run()

    # # To show the capabilities of the DummyApiPlugin:
    # valid = DummyApiPlugin("emilys", "emilyspass")
    # invalid = DummyApiPlugin("shaked", "notrealpassword")

    # # Test the connectivity test method of the DummyApiPlugin
    # def check_connectivity(plugin):
    #     if plugin.connectivity_test():
    #         print("Connectivity test succeeded.")
    #     else:
    #         print("Connectivity test failed.")

    # print("Testing connectivity test method...")
    # print("\nValid credentials:")
    # check_connectivity(valid)
    # print("\nInvalid credentials:")
    # check_connectivity(invalid)

    # # Test the collect method of the DummyApiPlugin
    # def collect_evidences(plugin):
    #     evidences = plugin.collect()
    #     if evidences:
    #         print("Evidences collected successfully!")
    #         for i, evidence in enumerate(evidences, 1):
    #             print("Evidence " + str(i) + ":")
    #             print(evidence)
    #     else:
    #         print("Failed to collect evidences.")
    #         return

    # print("\nTesting collect method...")
    # print("\nValid credentials:")
    # collect_evidences(valid)
    # print("\nInvalid credentials:")
    # collect_evidences(invalid)


if __name__ == '__main__':
    main()
