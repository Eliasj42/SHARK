# Copyright 2020 The Nod Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# All the iree_vulkan related functionalities go here.

from os import linesep
from shark.iree_utils._common import run_cmd


def get_vulkan_device_name():
    vulkaninfo_dump = run_cmd("vulkaninfo").split(linesep)
    vulkaninfo_list = [s.strip() for s in vulkaninfo_dump if "deviceName" in s]
    if len(vulkaninfo_list) == 0:
        raise ValueError("No device name found in VulkanInfo!")
    if len(vulkaninfo_list) > 1:
        print(
            f"Found {len(vulkaninfo_list)} device names. choosing first one: {vulkaninfo_list[0]}"
        )
    return vulkaninfo_list[0]


def get_vulkan_triple_flag(extra_args=[]):
    if "-iree-vulkan-target-triple=" in " ".join(extra_args):
        print(f"Using target triple from command line args")
        return None

    vulkan_device = get_vulkan_device_name()
    if all(x in vulkan_device for x in ("Apple", "M1")):
        print(f"Found {vulkan_device} Device. Using m1-moltenvk-macos")
        return "-iree-vulkan-target-triple=m1-moltenvk-macos"
    elif all(x in vulkan_device for x in ("Apple", "M2")):
        print("Found Apple M2 Device. Using m1-moltenvk-macos")
        return "-iree-vulkan-target-triple=m1-moltenvk-macos"
    elif all(x in vulkan_device for x in ("A100", "SXM4")):
        print(f"Found {vulkan_device} Device. Using ampere-rtx3080-linux")
        return "-iree-vulkan-target-triple=ampere-rtx3080-linux"
    elif all(x in vulkan_device for x in ("RTX", "3090")):
        print(f"Found {vulkan_device} Device. Using ampere-rtx3090-linux")
        return "-iree-vulkan-target-triple=ampere-rtx3090-linux"
    elif "AMD" in vulkan_device:
        print("Found AMD device. Using rdna2-unknown-linux")
        return "-iree-vulkan-target-triple=rdna2-unknown-linux"
    else:
        print(
            """Optimized kernel for your target device is not added yet.
            Contact SHARK Admin on discord[https://discord.com/invite/RUqY2h2s9u]
            or pull up an issue."""
        )
        print(f"Target : {vulkan_device}")
        return None


def get_iree_vulkan_args(extra_args=[]):
    # vulkan_flag = ["--iree-flow-demote-i64-to-i32"]
    vulkan_flag = []
    vulkan_triple_flag = get_vulkan_triple_flag(extra_args)
    if vulkan_triple_flag is not None:
        vulkan_flag.append(vulkan_triple_flag)
    return vulkan_flag
