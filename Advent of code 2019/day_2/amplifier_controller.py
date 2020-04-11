from program import Program


class AmplifierController():
    def __init__(self, program=[], phase_sequence=[]):
        self.program = program
        self.phase_sequence = phase_sequence

    def calculate_phase_sequence(self):
        if self.phase_sequence:
            return self.process_phase_sequence(self.phase_sequence)

    def process_phase_sequence(self, phase_sequence):
        program_a = Program(self.program, default_inputs=[phase_sequence[0], 0])
        program_b = Program(self.program, default_inputs=[phase_sequence[1], program_a.outputs.pop()])
        program_c = Program(self.program, default_inputs=[phase_sequence[2], program_b.outputs.pop()])
        program_d = Program(self.program, default_inputs=[phase_sequence[3], program_c.outputs.pop()])
        program_e = Program(self.program, default_inputs=[phase_sequence[4], program_d.outputs.pop()])
        return program_e.outputs.pop()
