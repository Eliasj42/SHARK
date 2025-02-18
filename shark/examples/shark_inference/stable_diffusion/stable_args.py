import argparse

p = argparse.ArgumentParser(
    description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

p.add_argument(
    "--prompts",
    nargs="+",
    default=["a photograph of an astronaut riding a horse"],
    help="text of which images to be generated.",
)
p.add_argument(
    "--device", type=str, default="cpu", help="device to run the model."
)
p.add_argument(
    "--steps",
    type=int,
    default=10,
    help="the no. of steps to do the sampling.",
)
p.add_argument(
    "--seed",
    type=int,
    default=42,
    help="the seed to use.",
)
p.add_argument(
    "--guidance_scale",
    type=float,
    default=7.5,
    help="the value to be used for guidance scaling.",
)

p.add_argument(
    "--import_mlir",
    default=False,
    action=argparse.BooleanOptionalAction,
    help="imports the model from torch module to shark_module otherwise downloads the model from shark_tank.",
)

p.add_argument(
    "--precision", type=str, default="fp32", help="precision to run the model."
)

p.add_argument(
    "--max_length",
    type=int,
    default=77,
    help="max length of the tokenizer output.",
)

p.add_argument(
    "--load_vmfb",
    default=True,
    action=argparse.BooleanOptionalAction,
    help="attempts to load the model from a precompiled flatbuffer and compiles + saves it if not found.",
)

p.add_argument(
    "--save_vmfb",
    default=False,
    action=argparse.BooleanOptionalAction,
    help="saves the compiled flatbuffer to the local directory",
)

p.add_argument(
    "--iree-vulkan-target-triple",
    type=str,
    default="",
    help="Specify target triple for vulkan",
)

p.add_argument(
    "--vulkan_debug_utils",
    default=False,
    action=argparse.BooleanOptionalAction,
    help="Profiles vulkan device and collects the .rdc info",
)

p.add_argument(
    "--use_tuned",
    default=True,
    action=argparse.BooleanOptionalAction,
    help="Download and use the tuned version of the model if available",
)

args = p.parse_args()
