from myhdl import *
#force std_logic_vectors
#toVHDL.numeric_ports = False
CONTENT = (
163, 160, 155, 155, 157, 170, 168, 136, 94, 105, 107, 108, 106, 117, 120, 125, 130, 130, 131, 131, 132, 133, 134, 133, 132, 134, 133, 131, 133, 131, 135, 131, 132, 132, 131, 128, 130, 128, 123, 110, 118, 150, 161, 150, 154, 154, 153, 156, 156, 157, 175, 216, 200, 99, 118, 123, 123, 123, 125, 122, 125, 125, 117, 149, 157, 158, 157, 152, 163, 169, 166, 130, 92, 100, 104, 105, 103, 112, 123, 127, 127, 132, 130, 132, 128, 132, 132, 131, 133, 132, 132, 129, 131, 131, 132, 131, 132, 129, 129, 128, 124, 128, 122, 112, 107, 137, 157, 156, 156, 159, 156, 154, 153, 155, 152, 206, 220, 137, 113, 118, 120, 120, 123, 123, 125, 128, 110, 45, 156, 157, 157, 153, 167, 165, 160, 132, 93, 98, 107, 103, 102, 113, 119, 124, 130, 131, 130, 128, 131, 133, 132, 131, 132, 132, 132, 133, 129, 128, 134, 131, 131, 131, 127, 127, 129, 127, 124, 120, 105, 123, 153, 160, 160, 162, 157, 156, 155, 153, 151, 166, 219, 206, 104, 117, 121, 123, 123, 127, 135, 105, 44, 49, 156, 160, 157, 165, 166, 159, 158, 133, 87, 98, 107, 102, 103, 111, 120, 123, 128, 130, 129, 130, 130, 129, 130, 132, 132, 127, 124, 127, 128, 125, 128, 131, 131, 128, 127, 125, 126, 129, 124, 119, 108, 121, 149, 161, 160, 160, 158, 155, 154, 153, 149, 143, 201, 222, 160, 109, 120, 119, 122, 128, 105, 47, 45, 54, 158, 159, 164, 168, 165, 157, 158, 131, 87, 98, 104, 102, 103, 111, 120, 122, 125, 128, 126, 126, 131, 129, 130, 127, 131, 126, 124, 123, 124, 122, 127, 129, 131, 127, 127, 125, 124, 127, 124, 117, 110, 120, 143, 154, 161, 159, 157, 156, 156, 154, 154, 150, 156, 216, 222, 118, 115, 122, 131, 102, 43, 54, 52, 52, 162, 161, 168, 158, 157, 162, 161, 128, 89, 99, 105, 103, 102, 112, 120, 124, 126, 126, 127, 125, 128, 130, 130, 127, 130, 127, 127, 127, 136, 128, 121, 123, 127, 127, 128, 126, 127, 127, 125, 116, 113, 117, 139, 147, 154, 155, 152, 152, 156, 155, 149, 144, 139, 193, 222, 185, 101, 117, 104, 42, 48, 55, 50, 45, 161, 168, 158, 141, 158, 163, 161, 131, 86, 99, 106, 102, 104, 115, 121, 123, 128, 125, 129, 131, 127, 125, 127, 129, 143, 143, 156, 170, 180, 180, 184, 166, 134, 116, 128, 129, 125, 126, 122, 116, 111, 114, 142, 144, 149, 154, 153, 154, 150, 147, 143, 143, 141, 150, 216, 225, 140, 101, 40, 46, 53, 52, 46, 46, 164, 169, 138, 123, 159, 165, 164, 132, 80, 94, 102, 100, 104, 114, 119, 121, 122, 125, 126, 125, 134, 140, 128, 132, 139, 143, 152, 163, 167, 174, 184, 185, 199, 172, 118, 124, 121, 122, 117, 112, 104, 119, 142, 145, 146, 151, 151, 147, 146, 146, 143, 140, 142, 139, 178, 224, 201, 35, 46, 54, 53, 51, 50, 49, 170, 156, 101, 119, 163, 169, 163, 132, 77, 91, 99, 101, 103, 106, 116, 116, 124, 124, 125, 134, 111, 120, 119, 133, 130, 137, 141, 155, 172, 179, 182, 188, 192, 195, 194, 129, 107, 115, 115, 110, 104, 114, 145, 148, 148, 144, 145, 144, 140, 145, 142, 139, 144, 144, 144, 215, 87, 43, 50, 54, 48, 50, 47, 46, 167, 133, 77, 119, 162, 168, 161, 130, 76, 90, 101, 101, 101, 107, 114, 114, 120, 123, 124, 127, 110, 116, 126, 128, 133, 134, 140, 150, 162, 181, 185, 191, 194, 196, 191, 206, 169, 96, 111, 104, 105, 111, 148, 155, 150, 127, 128, 148, 142, 147, 142, 143, 144, 148, 158, 80, 42, 49, 53, 45, 54, 50, 59, 72, 152, 94, 86, 118, 162, 168, 162, 127, 79, 95, 100, 101, 102, 108, 114, 119, 123, 123, 127, 107, 116, 120, 122, 122, 129, 138, 134, 146, 162, 183, 188, 186, 187, 200, 210, 211, 216, 176, 87, 99, 99, 109, 146, 153, 152, 122, 80, 138, 146, 146, 143, 148, 143, 151, 111, 37, 48, 54, 46, 51, 50, 65, 71, 151, 114, 87, 87, 118, 160, 167, 162, 126, 78, 92, 97, 103, 102, 110, 111, 117, 123, 125, 109, 114, 116, 117, 118, 127, 137, 140, 142, 145, 157, 177, 169, 193, 209, 207, 204, 206, 212, 228, 131, 84, 93, 112, 145, 156, 153, 129, 50, 102, 146, 147, 144, 141, 144, 147, 47, 47, 55, 51, 52, 46, 59, 85, 144, 144, 87, 90, 86, 117, 158, 168, 162, 127, 77, 94, 98, 100, 105, 105, 116, 117, 123, 118, 114, 112, 116, 117, 126, 132, 135, 143, 136, 141, 152, 167, 200, 201, 201, 196, 203, 204, 206, 209, 219, 147, 73, 104, 145, 155, 157, 129, 52, 63, 129, 148, 139, 145, 155, 68, 44, 55, 56, 50, 49, 53, 64, 136, 146, 162, 90, 95, 89, 120, 158, 164, 162, 129, 78, 92, 99, 99, 102, 107, 117, 116, 141, 102, 111, 112, 117, 123, 130, 141, 137, 141, 128, 132, 175, 193, 195, 189, 193, 204, 206, 202, 206, 205, 210, 225, 106, 98, 143, 155, 153, 129, 54, 40, 85, 132, 140, 142, 113, 41, 51, 56, 48, 52, 52, 49, 129, 141, 156, 163, 92, 90, 86, 115, 156, 164, 161, 128, 78, 89, 95, 99, 103, 108, 111, 107, 158, 103, 113, 110, 118, 127, 136, 135, 134, 120, 136, 184, 181, 186, 181, 195, 198, 197, 201, 203, 201, 208, 209, 212, 211, 73, 145, 153, 157, 131, 56, 41, 69, 199, 209, 217, 46, 51, 56, 56, 56, 53, 45, 103, 144, 153, 162, 156, 91, 92, 91, 114, 158, 167, 162, 127, 73, 87, 97, 99, 101, 105, 114, 139, 142, 102, 113, 112, 121, 127, 123, 131, 114, 149, 178, 168, 176, 177, 189, 187, 192, 191, 198, 199, 202, 201, 208, 207, 219, 128, 140, 157, 154, 128, 38, 106, 197, 208, 217, 227, 98, 45, 57, 46, 47, 57, 71, 151, 151, 161, 161, 158, 98, 101, 98, 115, 157, 172, 164, 132, 77, 92, 102, 102, 102, 109, 113, 163, 122, 102, 106, 117, 120, 121, 132, 117, 150, 161, 165, 174, 181, 184, 183, 180, 182, 192, 197, 195, 203, 186, 201, 203, 203, 209, 149, 155, 150, 111, 162, 197, 209, 209, 203, 223, 106, 51, 53, 47, 53, 41, 139, 148, 160, 160, 157, 156, 101, 101, 96, 120, 158, 170, 170, 134, 77, 90, 101, 101, 98, 106, 103, 177, 121, 102, 104, 111, 120, 121, 119, 143, 150, 145, 161, 177, 171, 181, 169, 175, 181, 182, 187, 191, 182, 188, 196, 198, 194, 194, 193, 149, 171, 200, 196, 208, 201, 204, 209, 225, 80, 50, 51, 44, 51, 91, 151, 156, 160, 158, 156, 157, 99, 100, 100, 119, 160, 173, 174, 134, 78, 91, 97, 100, 100, 105, 93, 201, 135, 110, 104, 112, 119, 121, 144, 145, 136, 153, 157, 165, 173, 166, 175, 177, 172, 182, 184, 178, 185, 191, 189, 181, 186, 177, 190, 189, 194, 205, 204, 200, 203, 199, 208, 230, 37, 50, 47, 51, 66, 148, 148, 162, 159, 156, 157, 154, 98, 97, 96, 118, 162, 172, 171, 137, 80, 92, 100, 99, 99, 104, 89, 204, 148, 126, 107, 110, 114, 138, 144, 128, 150, 149, 148, 160, 166, 170, 169, 171, 168, 167, 172, 181, 182, 181, 179, 171, 171, 183, 191, 201, 201, 196, 198, 201, 205, 163, 181, 165, 45, 51, 48, 51, 111, 147, 159, 160, 160, 159, 158, 156, 97, 96, 95, 119, 162, 170, 170, 135, 79, 94, 100, 97, 98, 102, 90, 197, 158, 138, 109, 105, 137, 135, 125, 144, 142, 146, 150, 155, 158, 164, 164, 163, 159, 164, 168, 167, 169, 170, 161, 172, 184, 196, 197, 193, 195, 203, 202, 208, 174, 161, 168, 101, 46, 48, 48, 80, 152, 154, 161, 158, 157, 160, 157, 156, 97, 97, 101, 122, 161, 172, 172, 138, 77, 95, 97, 97, 99, 101, 97, 206, 168, 152, 120, 129, 130, 122, 140, 138, 132, 143, 152, 133, 128, 132, 142, 129, 159, 157, 163, 147, 155, 156, 179, 190, 198, 186, 192, 199, 201, 204, 205, 204, 143, 110, 201, 34, 50, 54, 49, 127, 148, 158, 158, 157, 158, 156, 156, 153, 99, 98, 102, 126, 162, 174, 171, 139, 75, 91, 99, 100, 100, 100, 86, 213, 180, 143, 124, 120, 115, 139, 135, 127, 132, 143, 131, 129, 111, 81, 150, 110, 90, 92, 63, 57, 114, 172, 194, 194, 195, 194, 196, 201, 202, 210, 167, 112, 84, 171, 119, 45, 46, 51, 66, 148, 155, 161, 160, 157, 154, 155, 155, 153, 104, 102, 103, 124, 162, 173, 171, 139, 77, 93, 97, 99, 101, 98, 81, 199, 190, 133, 134, 107, 134, 131, 125, 130, 137, 121, 134, 99, 86, 60, 106, 83, 96, 76, 33, 120, 166, 190, 193, 191, 192, 192, 196, 208, 175, 91, 87, 124, 181, 110, 41, 49, 48, 54, 114, 147, 163, 160, 161, 158, 157, 156, 154, 153, 107, 107, 101, 124, 160, 172, 172, 139, 76, 89, 99, 97, 97, 100, 94, 156, 196, 153, 130, 127, 127, 123, 125, 128, 126, 119, 71, 67, 48, 83, 68, 93, 69, 62, 129, 169, 186, 183, 182, 185, 190, 196, 170, 99, 114, 154, 167, 184, 117, 41, 55, 50, 52, 60, 149, 155, 164, 165, 163, 158, 157, 155, 155, 153, 107, 104, 101, 119, 161, 173, 172, 142, 75, 90, 97, 97, 99, 100, 104, 102, 208, 180, 119, 129, 121, 126, 126, 130, 90, 74, 64, 77, 37, 65, 62, 71, 88, 109, 173, 192, 182, 182, 175, 183, 188, 184, 72, 103, 121, 151, 188, 97, 39, 52, 57, 46, 53, 96, 136, 167, 165, 163, 162, 162, 158, 158, 154, 152, 108, 105, 96, 111, 160, 173, 174, 141, 75, 85, 96, 97, 98, 102, 111, 101, 168, 194, 124, 114, 126, 122, 123, 98, 68, 87, 50, 74, 60, 49, 61, 68, 101, 147, 184, 180, 174, 178, 174, 188, 196, 200, 127, 84, 105, 150, 76, 44, 53, 57, 52, 48, 53, 126, 141, 167, 165, 165, 162, 161, 160, 161, 157, 153, 106, 102, 97, 111, 158, 174, 173, 147, 77, 89, 100, 102, 98, 104, 113, 107, 162, 176, 110, 120, 122, 132, 82, 64, 43, 69, 64, 59, 95, 52, 45, 114, 140, 185, 189, 164, 177, 163, 188, 199, 199, 204, 157, 55, 76, 160, 53, 45, 56, 62, 48, 48, 79, 134, 153, 163, 165, 164, 162, 162, 160, 158, 156, 153, 106, 105, 97, 110, 160, 173, 175, 146, 79, 90, 100, 103, 101, 109, 123, 114, 129, 160, 114, 122, 119, 69, 47, 65, 59, 51, 57, 85, 85, 30, 128, 168, 154, 180, 176, 167, 160, 177, 195, 200, 205, 213, 186, 70, 47, 148, 59, 56, 58, 64, 48, 46, 122, 143, 157, 151, 149, 156, 157, 161, 160, 157, 156, 151, 105, 101, 96, 109, 159, 174, 178, 144, 82, 94, 100, 106, 103, 109, 116, 115, 115, 137, 126, 131, 80, 64, 44, 61, 61, 54, 55, 73, 55, 113, 155, 180, 161, 185, 161, 157, 170, 180, 195, 200, 206, 210, 205, 101, 40, 130, 65, 54, 60, 54, 52, 59, 141, 158, 163, 159, 158, 152, 144, 147, 146, 151, 154, 151, 100, 99, 94, 110, 161, 172, 176, 143, 81, 88, 101, 102, 102, 108, 118, 121, 129, 103, 134, 105, 72, 70, 40, 74, 43, 63, 57, 59, 84, 148, 170, 175, 188, 124, 138, 163, 181, 179, 189, 194, 196, 208, 207, 103, 40, 105, 88, 64, 67, 51, 52, 97, 134, 162, 158, 158, 165, 163, 154, 151, 146, 143, 141, 145, 101, 103, 98, 104, 160, 174, 177, 146, 80, 92, 102, 102, 100, 107, 115, 142, 104, 81, 120, 63, 71, 95, 44, 56, 59, 49, 77, 51, 149, 181, 171, 186, 134, 141, 131, 81, 118, 171, 179, 190, 192, 155, 111, 96, 46, 80, 109, 63, 58, 50, 52, 126, 141, 164, 156, 157, 155, 159, 156, 153, 155, 151, 144, 134, 98, 98, 93, 100, 160, 175, 176, 146, 81, 86, 101, 97, 96, 116, 152, 152, 136, 82, 65, 96, 91, 59, 72, 41, 81, 50, 35, 122, 175, 198, 176, 71, 56, 48, 62, 72, 129, 144, 171, 203, 135, 72, 54, 59, 48, 76, 125, 61, 53, 50, 57, 140, 157, 157, 154, 155, 156, 156, 153, 154, 154, 149, 145, 139, 96, 97, 85, 95, 160, 178, 180, 145, 79, 94, 99, 101, 93, 118, 158, 130, 79, 61, 66, 54, 116, 45, 43, 71, 46, 50, 71, 153, 184, 195, 101, 54, 85, 62, 213, 99, 112, 136, 175, 191, 67, 76, 132, 48, 41, 75, 132, 66, 51, 49, 92, 141, 159, 157, 153, 150, 152, 154, 150, 148, 147, 138, 129, 136, 102, 97, 85, 92, 160, 179, 179, 148, 86, 98, 110, 88, 94, 147, 154, 66, 69, 71, 68, 87, 115, 66, 45, 51, 47, 38, 135, 180, 192, 120, 137, 131, 116, 144, 168, 150, 123, 130, 185, 176, 135, 139, 92, 62, 50, 64, 142, 70, 45, 52, 121, 148, 153, 155, 150, 155, 153, 154, 147, 142, 136, 140, 165, 183, 100, 90, 80, 84, 159, 180, 182, 149, 85, 99, 111, 125, 134, 77, 57, 54, 110, 78, 61, 91, 102, 77, 46, 48, 43, 92, 159, 194, 98, 131, 151, 157, 152, 150, 158, 158, 133, 129, 175, 202, 154, 132, 106, 79, 48, 58, 159, 58, 52, 53, 136, 153, 154, 152, 150, 149, 149, 148, 141, 131, 160, 190, 193, 188, 91, 82, 72, 81, 157, 177, 183, 149, 84, 97, 122, 133, 113, 89, 64, 100, 107, 44, 60, 86, 101, 99, 54, 45, 52, 135, 202, 88, 113, 130, 151, 166, 173, 177, 176, 157, 142, 129, 162, 211, 167, 141, 125, 88, 54, 45, 169, 47, 47, 80, 140, 158, 154, 152, 150, 148, 147, 143, 137, 161, 196, 195, 191, 191, 78, 76, 69, 80, 157, 177, 179, 149, 85, 98, 108, 108, 96, 84, 75, 107, 67, 51, 50, 54, 44, 113, 75, 39, 95, 171, 131, 58, 118, 130, 145, 159, 175, 179, 171, 154, 144, 128, 156, 214, 162, 147, 131, 77, 50, 50, 163, 49, 53, 108, 151, 155, 155, 149, 150, 147, 143, 136, 141, 193, 195, 193, 199, 203, 78, 78, 61, 76, 155, 173, 177, 149, 77, 112, 131, 93, 109, 74, 84, 112, 81, 58, 37, 72, 58, 148, 101, 32, 131, 197, 34, 70, 115, 131, 144, 154, 165, 170, 165, 147, 133, 120, 144, 219, 155, 143, 130, 60, 61, 44, 148, 69, 47, 135, 156, 154, 152, 151, 147, 144, 141, 132, 179, 195, 192, 202, 207, 202, 82, 76, 58, 71, 154, 177, 177, 150, 77, 108, 117, 81, 96, 74, 84, 115, 80, 47, 41, 90, 113, 79, 32, 109, 154, 80, 37, 84, 111, 127, 141, 152, 153, 161, 157, 134, 130, 133, 140, 215, 159, 142, 121, 42, 63, 46, 132, 91, 62, 145, 158, 153, 149, 151, 150, 145, 138, 147, 196, 194, 202, 209, 208, 209, 84, 77, 64, 83, 157, 173, 178, 154, 95, 95, 117, 77, 103, 73, 72, 100, 124, 49, 61, 46, 89, 42, 62, 183, 139, 37, 40, 95, 112, 126, 135, 146, 151, 156, 156, 136, 125, 101, 116, 183, 148, 137, 81, 45, 65, 55, 111, 103, 89, 149, 157, 153, 151, 148, 145, 144, 134, 174, 195, 198, 206, 205, 207, 208, 78, 78, 67, 110, 159, 171, 180, 154, 85, 94, 121, 68, 72, 80, 85, 106, 120, 78, 109, 44, 72, 126, 122, 156, 38, 59, 43, 97, 116, 127, 135, 142, 147, 155, 160, 153, 140, 152, 166, 183, 147, 133, 49, 50, 76, 59, 90, 111, 120, 153, 154, 151, 148, 150, 147, 143, 133, 189, 196, 208, 206, 212, 210, 210, 72, 72, 63, 111, 161, 170, 178, 153, 82, 95, 129, 68, 92, 58, 69, 83, 93, 111, 88, 58, 131, 171, 107, 64, 50, 62, 40, 110, 112, 128, 132, 139, 141, 148, 151, 147, 151, 191, 190, 185, 143, 92, 50, 55, 75, 60, 65, 127, 140, 154, 154, 148, 148, 144, 145, 137, 138, 195, 202, 207, 204, 207, 213, 210, 63, 68, 64, 110, 163, 173, 181, 156, 81, 110, 119, 62, 71, 67, 87, 88, 77, 111, 83, 151, 189, 101, 97, 62, 47, 59, 49, 91, 102, 129, 130, 138, 141, 120, 124, 130, 127, 132, 143, 130, 139, 46, 50, 59, 71, 65, 56, 141, 146, 156, 154, 148, 147, 148, 144, 140, 137, 200, 210, 210, 208, 211, 213, 213, 55, 64, 66, 114, 162, 177, 180, 152, 117, 93, 122, 67, 50, 74, 109, 80, 101, 80, 123, 158, 131, 139, 43, 44, 52, 59, 55, 82, 89, 120, 125, 135, 145, 138, 115, 123, 141, 160, 159, 142, 94, 48, 45, 57, 85, 68, 48, 152, 151, 156, 154, 149, 149, 148, 145, 139, 144, 209, 211, 208, 212, 213, 212, 210, 52, 58, 66, 106, 159, 179, 182, 159, 74, 119, 87, 92, 49, 69, 129, 104, 84, 126, 136, 152, 163, 50, 56, 54, 54, 61, 59, 75, 74, 105, 116, 128, 137, 142, 131, 128, 124, 131, 144, 133, 48, 48, 54, 58, 81, 73, 52, 158, 152, 156, 155, 154, 152, 149, 143, 137, 145, 216, 213, 214, 216, 210, 206, 205, 49, 51, 83, 111, 152, 176, 180, 155, 76, 112, 80, 72, 60, 49, 124, 126, 107, 107, 98, 171, 69, 54, 54, 53, 51, 54, 62, 55, 64, 80, 109, 123, 137, 139, 142, 145, 164, 160, 151, 78, 43, 55, 57, 56, 85, 74, 49, 166, 151, 156, 155, 155, 150, 147, 142, 130, 147, 219, 215, 214, 211, 213, 208, 210, 49, 47, 78, 115, 152, 175, 178, 156, 77, 91, 50, 78, 63, 45, 119, 65, 122, 127, 124, 82, 55, 52, 61, 55, 53, 48, 55, 55, 59, 61, 59, 100, 122, 137, 149, 164, 167, 165, 145, 44, 57, 63, 54, 67, 85, 81, 55, 161, 148, 154, 150, 148, 150, 144, 138, 126, 164, 221, 211, 214, 213, 208, 201, 156, 48, 44, 65, 104, 156, 174, 176, 150, 107, 122, 55, 66, 60, 42, 123, 81, 95, 108, 145, 124, 60, 50, 71, 54, 49, 52, 49, 59, 59, 70, 72, 92, 111, 126, 139, 155, 161, 159, 148, 59, 52, 57, 48, 66, 91, 84, 60, 162, 120, 125, 137, 142, 146, 145, 135, 120, 184, 215, 211, 209, 205, 168, 77, 43, 79, 55, 56, 79, 149, 171, 173, 164, 104, 88, 39, 71, 60, 68, 88, 111, 102, 109, 109, 94, 145, 62, 72, 60, 49, 53, 50, 58, 54, 61, 110, 126, 128, 135, 143, 146, 143, 163, 195, 209, 156, 71, 44, 66, 88, 79, 70, 156, 129, 122, 113, 106, 111, 119, 120, 111, 201, 207, 206, 209, 166, 58, 57, 83, 138, 106, 76, 56, 144, 171, 173, 155, 113, 76, 40, 95, 51, 97, 53, 102, 110, 83, 113, 127, 101, 91, 61, 57, 52, 52, 55, 52, 67, 58, 107, 122, 126, 136, 142, 141, 150, 173, 191, 193, 202, 214, 133, 49, 79, 76, 76, 151, 145, 140, 133, 123, 108, 97, 111, 86, 195, 208, 212, 166, 57, 76, 85, 85, 131, 151, 112, 55, 146, 175, 174, 150, 159, 44, 46, 58, 77, 63, 80, 73, 61, 78, 104, 141, 95, 115, 77, 57, 55, 52, 60, 58, 86, 57, 108, 120, 135, 138, 140, 142, 160, 169, 178, 187, 195, 205, 214, 151, 57, 71, 78, 147, 149, 146, 144, 138, 130, 122, 127, 115, 211, 213, 199, 75, 90, 89, 106, 91, 68, 155, 150, 57, 146, 179, 178, 154, 119, 39, 53, 56, 43, 85, 46, 63, 86, 79, 96, 121, 145, 81, 93, 52, 58, 48, 64, 51, 100, 65, 103, 133, 134, 138, 141, 145, 154, 163, 171, 182, 190, 202, 210, 223, 102, 55, 85, 143, 147, 145, 142, 139, 135, 128, 133, 154, 216, 212, 157, 79, 94, 109, 97, 101, 38, 150, 163, 46, 147, 179, 181, 159, 108, 43, 57, 46, 49, 84, 58, 62, 63, 92, 94, 118, 132, 51, 121, 54, 62, 48, 54, 54, 103, 75, 107, 128, 134, 139, 140, 146, 152, 159, 169, 179, 187, 199, 209, 214, 207, 33, 95, 144, 146, 146, 141, 137, 132, 123, 170, 203, 217, 209, 109, 93, 109, 103, 96, 100, 32, 137, 166, 44, 144, 180, 182, 159, 90, 55, 45, 42, 86, 68, 56, 47, 48, 65, 101, 112, 133, 128, 100, 57, 58, 55, 53, 74, 125, 80, 113, 134, 136, 139, 136, 144, 148, 158, 164, 175, 186, 197, 208, 210, 224, 79, 102, 149, 146, 144, 139, 135, 128, 133, 218, 209, 217, 176, 93, 97, 113, 93, 106, 97, 31, 127, 170, 58, 143, 177, 176, 158, 97, 47, 47, 55, 60, 71, 58, 47, 50, 69, 68, 133, 99, 103, 92, 84, 85, 53, 53, 96, 127, 77, 118, 132, 142, 136, 134, 139, 145, 153, 160, 169, 183, 194, 203, 212, 216, 140, 112, 149, 142, 141, 139, 136, 127, 152, 213, 209, 213, 131, 105, 103, 105, 95, 99, 89, 36, 108, 170, 68, 138, 178, 179, 159, 96, 50, 45, 67, 52, 59, 47, 53, 54, 78, 88, 117, 112, 81, 48, 55, 67, 52, 66, 112, 132, 75, 126, 139, 139, 140, 135, 138, 146, 150, 159, 164, 177, 191, 201, 206, 213, 193, 119, 146, 144, 142, 141, 136, 131, 145, 195, 214, 192, 114, 102, 99, 87, 104, 94, 94, 36, 96, 167, 82, 135, 177, 175, 157, 113, 44, 60, 45, 56, 58, 58, 54, 59, 65, 77, 76, 71, 129, 57, 51, 46, 47, 87, 119, 111, 86, 135, 140, 145, 141, 136, 137, 143, 148, 155, 160, 172, 187, 196, 207, 213, 219, 130, 96, 116, 136, 141, 142, 145, 142, 145, 220, 169, 104, 92, 82, 99, 93, 95, 84, 32, 86, 179, 92, 127, 173, 180, 164, 98, 55, 46, 54, 58, 51, 62, 45, 57, 71, 123, 72, 86, 60, 44, 47, 42, 65, 109, 122, 60, 122, 133, 140, 141, 144, 138, 140, 138, 146, 151, 157, 167, 180, 194, 204, 211, 218, 135, 85, 81, 79, 81, 95, 141, 153, 175, 214, 120, 75, 88, 91, 96, 94, 101, 62, 70, 95, 183, 112, 128, 174, 177, 160, 99, 47, 51, 51, 53, 58, 61, 49, 48, 53, 85, 133, 103, 43, 44, 41, 47, 90, 118, 82, 85, 135, 139, 140, 139, 142, 141, 138, 138, 142, 149, 156, 162, 175, 188, 199, 209, 213, 182, 95, 103, 90, 63, 38, 109, 190, 198, 177, 64, 76, 83, 103, 83, 104, 88, 57, 89, 122, 179, 126, 126, 175, 183, 153, 98, 46, 46, 50, 50, 54, 62, 59, 62, 62, 62, 96, 88, 44, 45, 37, 73, 109, 72, 72, 127, 132, 138, 139, 139, 145, 143, 142, 140, 139, 146, 150, 161, 169, 180, 196, 207, 213, 219, 85, 107, 99, 86, 71, 114, 207, 165, 67, 67, 74, 103, 77, 87, 107, 85, 65, 65, 104, 172, 136, 123, 175, 183, 165, 68, 45, 56, 51, 58, 64, 63, 94, 63, 55, 76, 110, 79, 42, 42, 43, 59, 66, 104, 121, 129, 134, 134, 139, 141, 145, 146, 143, 141, 142, 143, 148, 156, 167, 179, 189, 201, 211, 217, 113, 95, 105, 101, 106, 115, 150, 77, 78, 74, 107, 81, 69, 109, 106, 67, 62, 58, 77, 177, 165, 121, 176, 181, 155, 56, 49, 55, 59, 63, 74, 48, 106, 54, 79, 82, 76, 80, 41, 45, 75, 107, 114, 125, 128, 130, 132, 136, 138, 139, 140, 144, 146, 146, 144, 143, 147, 153, 162, 173, 183, 195, 205, 211, 150, 88, 107, 115, 117, 114, 100, 108, 86, 95, 79, 73, 97, 118, 87, 59, 55, 50, 60, 193, 192, 121, 175, 182, 152, 54, 51, 62, 66, 65, 88, 57, 78, 87, 87, 59, 64, 90, 67, 68, 96, 113, 120, 125, 126, 128, 132, 135, 133, 139, 141, 144, 145, 145, 148, 148, 150, 156, 164, 168, 179, 190, 203, 207, 190, 83, 98, 115, 125, 118, 128, 115, 91, 85, 85, 89, 127, 99, 57, 56, 85)

SUB2 = 256
SUB3 = 512
ROM_ADDR = 12
dout_rom = Signal(intbv(0)[16:])
addr_rom_r = Signal(intbv(0)[ROM_ADDR:])
addr_rom_x = Signal(intbv(0)[ROM_ADDR:])
def rom(dout_rom, addr_rom_r, CONTENT):
    """ ROM model """

    @always_comb
    def read():
        dout_rom.next = CONTENT[int(addr_rom_r)]

    return read
reset_dly_c = 10
ASZ = 10
DSZ = 16
 
enw_r = Signal(bool(0))
enr_r = Signal(bool(0))
empty_r = Signal(bool(0))
full_r = Signal(bool(0))
dataout_r = Signal(intbv(0)[DSZ:])
datain_r = Signal(intbv(0)[DSZ:])

enw_x = Signal(bool(0))
enr_x = Signal(bool(0))
empty_x = Signal(bool(0))
full_x = Signal(bool(0))
dataout_x = Signal(intbv(0)[DSZ:])
datain_x = Signal(intbv(0)[DSZ:])

readptr = Signal(intbv(0)[ASZ:])
writeptr = Signal(intbv(0)[ASZ:])
mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
def jpegfifo(clk_fast, empty_r, full_r, enr_r, enw_r, dataout_r, datain_r ):
    """Following the code being converted requires the that both readptr
    writeptr be initialized :="00000000" """
    readptr = Signal(intbv(0)[ASZ:])
    writeptr = Signal(intbv(0)[ASZ:])
    reset_ctn = Signal(intbv(val=0, min=0, max=16))
    mem = [Signal(intbv(0)[DSZ:]) for ii in range(2**ASZ)]
    @always(clk_fast.posedge)
    def rtl():     
        if (reset_ctn < reset_dly_c):
            readptr.next = 0
            writeptr.next = 0
            reset_ctn.next = reset_ctn + 1
        if ( enr_r == YES):
            dataout_x.next = mem[int(readptr)]
            readptr.next = readptr + 1
        if (enw_r == YES):
            mem[int(writeptr)].next = datain_x    
            writeptr.next = writeptr + 1
        if  (readptr == 1023):
            readptr.next = 0
        if (writeptr == 1023):
            full_x.next = YES
            writeptr.next = 0
        else:
            empty_x.next = NO
    return rtl 
 
clk_fast = Signal(bool(0))
rst = ResetSignal(0,active=1,async=True)

reset_dly_c = 10
DATA_WIDTH = 32768
JPEG_RAM_ADDR = 23
JPEG_RES_RAM_ADDR = 9
ROW_NUM = 8
ACTIVE_LOW = bool(0)
NO = bool(0)
YES = bool(1)
 
 
#rst_file_in = Signal(bool(1))
#eog = Signal(bool(0))
#y_u = Signal(intbv(0)[16:])

rd0_s = Signal(bool(0))
wr0_s = Signal(bool(0))
rd1_s = Signal(bool(0))
wr1_s = Signal(bool(0)) 
done0_s = Signal(bool(0))
done1_s = Signal(bool(0))
dataToRam0_r = Signal(intbv(0)[16:])
dataToRam0_x = Signal(intbv(0)[16:])
dataFromRam0_s = Signal(intbv(0)[16:])
dataFromRam0_r = Signal(intbv(0)[16:])
dataFromRam0_x = Signal(intbv(0)[16:])

dataToRam1_r = Signal(intbv(0)[16:])
dataToRam1_x = Signal(intbv(0)[16:])
dataFromRam1_s = Signal(intbv(0)[16:])
dataFromRam1_r = Signal(intbv(0)[16:])
dataFromRam1_x = Signal(intbv(0)[16:])
addr0_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr0_x = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr1_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
addr1_x = Signal(intbv(0)[JPEG_RAM_ADDR:])
sum_r = Signal(intbv(0)[16:])
sum_x = Signal(intbv(0)[16:])
 
 
 
 
col_x = Signal(intbv(0)[ROW_NUM:])
col_r = Signal(intbv(0)[ROW_NUM:])
row_x = Signal(intbv(0)[ROW_NUM:])
row_r = Signal(intbv(0)[ROW_NUM:])


index1_r = Signal(intbv(513)[JPEG_RAM_ADDR:])
index2_r = Signal(intbv(513)[JPEG_RAM_ADDR:])
index3_r = Signal(intbv(513)[JPEG_RAM_ADDR:])
index1_x = Signal(intbv(513)[JPEG_RAM_ADDR:])
index2_x = Signal(intbv(513)[JPEG_RAM_ADDR:])
index3_x = Signal(intbv(513)[JPEG_RAM_ADDR:])


sig_in = Signal(intbv(0)[52:])
 
noupdate_s = Signal(bool(0))
res_s = Signal(intbv(0, min = -DATA_WIDTH, max = DATA_WIDTH))
res_u = Signal(intbv(0)[16:])
jp_lf = Signal(intbv(0)[16:])
jp_sa = Signal(intbv(0)[16:])
jp_rh = Signal(intbv(0)[16:])
jp_flgs = Signal(intbv(0)[4:])
jp_row_lf = Signal(intbv(0)[16:])
jp_row_sa = Signal(intbv(0)[16:])
jp_row_rh = Signal(intbv(0)[16:])
jp_row_flgs = Signal(intbv(0)[4:])

din_res_r = Signal(intbv(0)[16:])
dout_res_r = Signal(intbv(0)[16:])
dout_res_r1 = Signal(intbv(0)[16:])
dout_res_r2 = Signal(intbv(0)[16:])
din_res_x = Signal(intbv(0)[16:])
dout_res_x = Signal(intbv(0)[16:])
offset = Signal(intbv(0)[JPEG_RAM_ADDR:])
reset_col = Signal(bool(1))
reset_col_r = Signal(bool(1))
reset_row = Signal(bool(1))
reset_row_r = Signal(bool(1))
we_res = Signal(bool(1))
addr_not_reached = Signal(bool(1))
addr_not_reached1 = Signal(bool(1))
addr_not_reached2 = Signal(bool(1))
rdy = Signal(bool(0))
reset_ctn = Signal(intbv(0)[4:])
 
 
offset_x = Signal(intbv(0)[JPEG_RAM_ADDR:])
offset_r = Signal(intbv(0)[JPEG_RAM_ADDR:])
#t_State = enum('INIT', 'ODD_SA', 'EVEN_SA','ODD_SA_COL', 'EVEN_SA_COL', 'TR_RES', 'TR_INIT', 'TRAN_RAM', 'DONE_PASS1', encoding="one_hot")
#t_State = enum('INIT', 'WRITE_DATA', 'READ_AND_SUM_DATA', 'DONE', encoding="one_hot")
t_State = enum('INIT', 'READ_ROM_TO_FIFO', 'WRITE_FIFO_TO_SDRAM', 'WRITE', 'READ_AND_SUM_DATA', 'CK_SDRAM_RD', 'CK_SDRAM_WR', 'ODD_SAMPLES', 'EVEN_SAMPLES', 'WR_DATA', 'INTERLACE', 'DONE', encoding="one_hot")
#print t_State, t_State.INIT
state_r = Signal(t_State.INIT)
state_x = Signal(t_State.INIT)
state = Signal(t_State.INIT)
even_odd_r = Signal(bool(0))
even_odd_x = Signal(bool(0))
#print  t_State.INIT, t_State.READ_AND_SUM_DATA, state_r, state_x


reset_col = Signal(bool(1))
 
def resetFsm(clk_fast, reset_fsm_r, reset_ctn):
    @always(clk_fast.posedge)
    def rtl():
        reset_fsm_r.next = YES
        if (reset_ctn < reset_dly_c):
            reset_fsm_r.next = NO
            reset_ctn.next = reset_ctn + 1
    return rtl
 
def muxaddr(addr_r, addr_r1, addr_r2, muxsel_r, dataFromRam0_r, dataFromRam_r1, dataFromRam_r2 ):
	@always_comb
	def muxLogic():
		addr_r.next = addr_r1
		dataFromRam0_r.next = dataFromRam_r1
		 
		if (muxsel_r == 1):
			addr_r.next = addr_r2
			dataFromRam0_r.next = dataFromRam_r2
			 
	return muxLogic		
		


#instance_6_dn_interface_rd_en, instance_14_dout, instance_6_dn_interface_wr_en,
#instance_13_din, instance_13_full, instance_14_empty):
def RamCtrl(addr0_r, addr0_x,  addr1_r, addr1_x, state_r, state_x,
            dataToRam0_r, dataToRam0_x,
            dataFromRam0_r, dataFromRam0_x,  dataFromRam0_s,
            dataToRam1_r, dataToRam1_x,
            dataFromRam1_r, dataFromRam1_x,  dataFromRam1_s,
            done0_s, wr0_s, rd0_s, done1_s, wr1_s, rd1_s, sum_r, sum_x,
            empty_r, full_r, enr_r, enw_r, dataout_r, datain_r,
            empty_x, full_x, enr_x, enw_x, dataout_x, datain_x,
            offset_r, offset_x, reset_col, jp_flgs,
            jp_lf, jp_sa, jp_rh,
            col_r, col_x, row_r, row_x, addr_not_reached,
            dout_rom, addr_rom_r, addr_rom_x, rdy, res_u, noupdate_s,
            index1_r, index2_r, index3_r, index1_x, index2_x, index3_x):
    @always_comb
    def FSM():
        TEST1 = index1_r
        TEST2 = index2_r
        TEST3 = index3_r
        addr0_x.next = addr0_r
        addr1_x.next = addr1_r
        state_x.next = state_r
        sum_x.next = sum_r
        wr0_s.next = NO
        rd0_s.next = NO
        wr1_s.next = NO
        rd1_s.next = NO
        dataToRam0_x.next = dataToRam0_r
        dataFromRam0_x.next = dataFromRam0_r
        dataToRam1_x.next = dataToRam1_r
        dataFromRam1_x.next = dataFromRam1_r
        enr_x.next = enr_r
        enw_x.next = enw_r
        #dataout_x.next = dataout_r
        datain_x.next = datain_r
        offset_x.next = offset_r
        col_x.next = col_r
        row_x.next = row_r
        addr_rom_x.next = addr_rom_r
        index1_x.next = index1_r
        index2_x.next = index2_r
        index3_x.next = index3_r
        if state_r == t_State.INIT:
             
            enr_x.next = NO
            enw_x.next = NO
            addr0_x.next = 65536
            dataToRam0_x.next = 0
            datain_x.next = 0
            offset_x.next = 0
            col_x.next = 0
            row_x.next = 0
            index1_x.next = 1
            index2_x.next = 257
            index3_x.next = 513
            state_x.next = t_State.WRITE
        elif state_r == t_State.WRITE:
            if (done0_s == NO):
                wr0_s.next = YES
                #enw_x.next = NO
                
            elif (addr0_r <= 65541):
                #enw_x.next = YES
                addr0_x.next = addr0_r + 1
                dataToRam0_x.next = dataToRam0_r + 1
                #datain_x.next = dataToRam_r + 1
            else:
                addr0_x.next = 65536
                enw_x.next = NO
                enr_x.next = NO
                sum_x.next = 0
                state_x.next = t_State.READ_AND_SUM_DATA
        elif state_r == t_State.READ_AND_SUM_DATA:
            if (done0_s == NO):
                rd0_s.next = YES
                #enr_x.next = NO
                #enw_x.next = NO
            elif (addr0_r <= 65541):
                #enr_x.next = YES
                #dataToRam_x.next = dataout_r
                sum_x.next = sum_r + (dataFromRam0_s )
                addr0_x.next = addr0_r + 1
            else:
                enr_x.next = NO
                addr0_x.next = 0
                addr_rom_x.next = 0
                """get ready for EVEN_SAMPLES """
                enr_x.next = NO
                addr0_x.next = 0
                offset_x.next = 0
                row_x.next = 0
                index2_x.next = 1
                index2_x.next = 257
                index3_x.next = 513
                state_x.next = t_State.READ_ROM_TO_FIFO
        elif state_r == t_State.CK_SDRAM_RD:
            if (done0_s == NO):
               #enr_x.next = YES
               rd0_s.next = YES
               enw_x.next = NO
            elif addr0_r <= 1023 :
                enw_x.next = YES
                addr0_x.next = addr0_r + 1
                datain_x.next = dataFromRam0_s
                #dataToRam_x.next = dataout_r
            else:
                addr0_x.next = 131072
                state_x.next = t_State.CK_SDRAM_WR
        elif state_r == t_State.CK_SDRAM_WR:
            if (done0_s == NO):
                wr0_s.next = YES
                enr_x.next = NO
            elif (addr0_r <= 132095):
                enr_x.next = YES
                dataToRam0_x.next =  dataout_r
                addr0_x.next = addr0_r + 1
            else:
                state_x.next = t_State.DONE
        elif state_r == t_State.ODD_SAMPLES:
            if (done0_s == NO):
               rd0_s.next = YES
               reset_col.next = 0
            elif (row_r <= 254):
                reset_col.next = 1
                jp_flgs.next = 6
                #if (addr_not_reached == 1):
                    #offset_x.next = offset_r + 256
                    #row_x.next = row_r + 1
                if (row_r == 254):
                    if (col_r <= 254):
                        row_x.next = 0
                        offset_x.next = offset_r - 65022
                        col_x.next = col_r + 1
                    else:
                        offset_x.next = 0
                        row_x.next = 0
                        col_x.next = 0
                        state_x.next = t_State.DONE
        elif state_r == t_State.READ_ROM_TO_FIFO:
            enw_x.next = YES
            
            if (offset_r <= 256):
                offset_x.next = offset_r + 1
                addr_rom_x.next = addr_rom_r + 1
                datain_x.next = dout_rom
            else:
                enw_x.next = NO
                addr0_x.next = 1
                state_x.next = t_State.WRITE_FIFO_TO_SDRAM
        elif state_r == t_State.WRITE_FIFO_TO_SDRAM:
            if (done0_s == NO):
                wr0_s.next = YES
                enr_x.next = YES
            elif (addr0_r <= 32769):
                addr0_x.next = addr0_r + 256
                dataToRam0_x.next = dataout_r
            else:
                enr_x.next = NO
                addr0_x.next = 0
                offset_x.next = 0
                row_x.next = 0
                index2_x.next = 1
                index2_x.next = 257
                index3_x.next = 513
                state_x.next = t_State.EVEN_SAMPLES
        elif state_r == t_State.EVEN_SAMPLES:
            if (done0_s == NO):
               rd0_s.next = YES
               reset_col.next = 0
               addr_not_reached.next = NO
               rdy.next = NO
               enw_x.next = NO
            elif (row_r <= 254):
                reset_col.next = 1
                jp_flgs.next = 7
                addr0_x.next = offset_r + 1
                offset_x.next = (offset_r + 256)
                row_x.next = row_r + 1
                if (addr0_r == TEST1):
                    jp_lf.next = dataFromRam0_s
                    index1_x.next = index1_r + 768
                if (addr0_r == TEST2):
                    jp_sa.next = dataFromRam0_s
                    index2_x.next = index2_r + 768 
                if (addr0_r == TEST3):
                    jp_rh.next = dataFromRam0_s
                    addr_not_reached.next = YES
                    rdy.next = YES
                    index3_x.next = index3_r + 768
            else:
                offset_x.next = (offset_r - 65278)
                index1_x.next = index1_r - 65278
                index2_x.next = index2_r - 65278
                index3_x.next = index3_r - 64510
                row_x.next = 0
                col_x.next = col_r + 1
                if (col_r == 254):
                    state_x.next = t_State.INIT
        elif state_r == t_State.WR_DATA:
            if addr0_r == 1:
                addr0_x.next = 8
            else:
                state_x.next = t_State.DONE
        elif state_r == t_State.INTERLACE:
            if addr0_r == 16:
                state_x.next = t_State.DONE
        elif state_r == t_State.DONE:
            #if addr_r.next == 1:
            state_x.next = t_State.INIT

            
            
    return FSM
    
 
def jpegfsmupdate(clk_fast, addr0_r, addr0_x, addr1_r, addr1_x, state_r,
                  state_x, dataToRam0_r, dataToRam0_x, dataToRam1_r, dataToRam1_x,
                  dataFromRam0_r, dataFromRam0_x, dataFromRam1_r, dataFromRam1_x,
                  sum_r, sum_x, 
                  empty_r, full_r, enr_r, enw_r, dataout_r, datain_r,
                  empty_x, full_x, enr_x, enw_x, dataout_x, datain_x,
                  offset_r, offset_x, col_r, col_x, row_r, row_x,
                  addr_rom_r, addr_rom_x,
                  index1_r, index2_r, index3_r, index1_x, index2_x, index3_x):
    @always(clk_fast.posedge)
    def fsmupdate():
 
        addr0_r.next = addr0_x
        dataToRam0_r.next = dataToRam0_x
        dataFromRam0_r.next = dataFromRam0_x
        addr1_r.next = addr1_x
        dataToRam1_r.next = dataToRam1_x
        dataFromRam1_r.next = dataFromRam1_x
        state_r.next = state_x
        sum_r.next = sum_x
        empty_r.next = empty_x
        full_r.next = full_x
        enr_r.next = enr_x
        enw_r.next = enw_x
        dataout_r.next = dataout_x
        datain_r.next = datain_x
        offset_r.next = offset_x
        col_r.next = col_x
        row_r.next = row_x
        addr_rom_r.next = addr_rom_x
        index1_r.next = index1_x
        index2_r.next = index2_x
        index3_r.next = index3_x
    return fsmupdate
def jpeg_process(clk_fast, sig_in,  noupdate_s, res_s, res_u):
    left_s = sig_in(16,0)
    sam_s = sig_in(32,16)
    right_s = sig_in(48,32)
    even_odd_s = sig_in(48)
    fwd_inv_s = sig_in(49)
    updated_s = sig_in(50)
    dum_s = sig_in(52)
    @always(clk_fast.posedge)
    def jpeg():
        if updated_s:
            noupdate_s.next = 0
            if even_odd_s:
                if  fwd_inv_s:
                    res_s.next =  sam_s - ((left_s >> 1) + (right_s >> 1))
                else:
                    res_s.next =  sam_s + ((left_s >> 1) + (right_s >> 1))
            else:
                if fwd_inv_s:
                    res_s.next =  sam_s + ((left_s +  right_s + 2)>>2)
                else:
                    res_s.next =  sam_s - ((left_s +  right_s + 2)>>2)
            res_u.next = res_s
        else:
            noupdate_s.next = 1
    return jpeg
def jpegsdram_rd(clk_fast, offset_x, dataFromRam0_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_col, addr0_r, addr_not_reached):
    even = jp_flgs(0)
    @always(clk_fast.posedge)
    def sdram_rd():
        
        
        if (  reset_col):
            jp_lf.next = 0
            jp_sa.next = 0
            jp_rh.next = 0
            addr_not_reached.next = 0
            #if jp_flgs 6 odd jp_flgs 7 even
            #if (even  == 1):           
                #addr_r.next = 1 + offset_x
            #else:
                #addr_r.next = 0 + offset_x
        else:
            if (even):
                    if (addr0_r == offset_x ):
                        jp_lf.next = dataFromRam0_s
                        #addr_r.next = addr_r + 256
                    else:
                        if (addr0_r == offset_x):
                            jp_sa.next = dataFromRam0_s
                            #addr_r.next = addr_r + 256
                        else:
                            if (addr0_r == offset_x):
                                jp_rh.next = dataFromRam0_s
                                addr_not_reached.next = 1
            else:
                if (addr0_r == (0 + offset_x)):
                    jp_lf.next = dataFromRam0_s
                    #addr_r.next = addr_r + 256
                else:
                    if (addr0_r == (256 + offset_x)):
                        jp_sa.next = dataFromRam0_s
                        #addr_r.next = addr_r + 256
                    else:
                        if (addr0_r == (512 + offset_x)):
                            jp_rh.next = dataFromRam0_s
                            addr_not_reached.next = 1
    return sdram_rd
def jpegsdram_rd_col(clk_fast, offset_x, dataFromRam_s, jp_row_lf, jp_row_sa, jp_row_rh, jp_row_flgs, reset_row, addr_r, addr_not_reached):
    even = jp_row_flgs(0)
    @always(clk_fast.posedge)
    def sdram_rd_col():
        
        
        if (reset_row):
            jp_row_lf.next = 0
            jp_row_sa.next = 0
            jp_row_rh.next = 0
            addr_not_reached.next = 0
            #if jp_row_flgs 6 odd jp_row_flgs 7 even_odd
            if (even  == 1):           
                addr_r.next = 1 + offset_x
            else:
                addr_r.next = 0 + offset_x
        else:
            if (even):
                    if (addr_r == (1 + offset_x) ):
                        jp_row_lf.next = dataFromRam_s
                        addr_r.next = addr_r + 1
                    else:
                        if (addr_r == (2 + offset_x)):
                            jp_row_sa.next = dataFromRam_s
                            addr_r.next = addr_r + 1
                        else:
                            if (addr_r == (3 + offset_x)):
                                jp_row_rh.next = dataFromRam_s
                                addr_not_reached.next = 1
            else:
                if (addr_r == (0 + offset_x)):
                    jp_row_lf.next = dataFromRam_s
                    addr_r.next = addr_r + 1
                else:
                    if (addr_r == (1 + offset_x)):
                        jp_row_sa.next = dataFromRam_s
                        addr_r.next = addr_r + 1
                    else:
                        if (addr_r == (2 + offset_x)):
                            jp_row_rh.next = dataFromRam_s
                            addr_not_reached.next = 1
    return sdram_rd_col
def jpegram2sig(jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached,  sig_in):
    """Combines 3 16 bit plus 4 flags into single value """
    @always_comb
    def ram2sig():
        if rdy:
            if addr_not_reached:
                sig_in.next = concat(jp_flgs, jp_rh, jp_sa, jp_lf)
            else:
                sig_in.next = 0
        else:
            sig_in.next = 0
    return ram2sig
def jpegram2sigcol(jp_row_lf, jp_row_sa ,jp_row_rh, jp_row_flgs, rdy, addr_not_reached,  sig_in):
    """Combines 3 16 bit plus 4 flags into single value """
    @always_comb
    def ram2sigcol():
        if rdy:
            if addr_not_reached:
                sig_in.next = concat(jp_row_flgs, jp_row_rh, jp_row_sa, jp_row_lf)
            else:
                sig_in.next = 0
        else:
            sig_in.next = 0
    return ram2sigcol

#def test_instances(clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y, addr_r1, addr_r2, sel, sig_in, noupdate_s, res_s, offset, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs, reset_col, addr_not_reached, rdy, state_r, state_x, reset_fsm_r, addr_res, addr_res_r, offset_r, addr_rom, addr_rom_r):
def ramres(dout_res_r, din_res_r, addr_res_r, we_res, clk_fast, depth=256):
    """  Ram model """
    
    mem = [Signal(intbv(0)[16:]) for i in range(depth)]
    
    @always(clk_fast.posedge)
    def write():
        if we_res:
            mem[addr_res_r].next = din_res_r
                
    @always_comb
    def read():
        dout_res_r.next = mem[addr_res_r]

    return write, read

def xess_jpeg_top(clk_fast,
                  addr0_r, addr0_x, addr1_r, addr1_x,
                  state_r, state_x,
                  dataToRam0_r, dataToRam0_x, dataFromRam0_r, dataFromRam0_x,
                  dataToRam1_r, dataToRam1_x, dataFromRam1_r, dataFromRam1_x,
                  sig_in, noupdate_s, res_s, res_u,
                  jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached,
                  offset_r, offset_x, dataFromRam0_s, done0_s, wr0_s, rd0_s, sum_r, sum_x,
                  empty_r, full_r, enr_r, enw_r, dataout_r, datain_r,
                  empty_x, full_x, enr_x, enw_x, dataout_x, datain_x,
                  col_r, col_x, row_r, row_x,
                  dout_rom, addr_rom_r, addr_rom_x, CONTENT,
                  index1_r, index2_r, index3_r, index1_x, index2_x, index3_x):
    """The following between the single quotes ':= "0000"' needs to added to line below
    signal instance_1_reset_ctn: unsigned(3 downto 0);
    before the ';' to be like the following
    signal instance_1_reset_ctn: unsigned(3 downto 0):= "0000";
     """
    instance_1 = jpegfifo(clk_fast,
                          empty_r,
                          full_r,
                          enr_r,
                          enw_r,
                          dataout_r,
                          datain_r) 
    #instance_13 = fifo_up_if.fifo_up_if_ex(clk_fast,rst,up_interface.din,up_interface.wr_en,up_interface.full)        
    #instance_14 = fifo_down_if.fifo_down_if_ex(clk_fast, rst, dn_interface.dout, dn_interface.rd_en, dn_interface.empty)
    
    #instance_2 = muxaddr(addr_r, addr_r1, addr_r2, muxsel_r, dataFromRam_r, dataFromRam_r1, dataFromRam_r2 )
    instance_3 = jpeg_process(clk_fast, sig_in,  noupdate_s, res_s, res_u)
    #instance_4 = jpegsdram_rd(clk_fast, offset_x, dataFromRam_s, jp_lf, jp_sa, jp_rh, jp_flgs,
    #                          reset_col, addr_r2, addr_not_reached)
    instance_5 = jpegram2sig(jp_lf, jp_sa ,jp_rh, jp_flgs, rdy, addr_not_reached, sig_in)
    instance_6 = RamCtrl(addr0_r, addr0_x,  addr1_r, addr1_x, state_r, state_x,
                         dataToRam0_r, dataToRam0_x,
                         dataFromRam0_r, dataFromRam0_x,  dataFromRam0_s,
                         dataToRam1_r, dataToRam1_x,
                         dataFromRam1_r, dataFromRam1_x,  dataFromRam1_s,
                         done0_s, wr0_s, rd0_s, done1_s, wr1_s, rd1_s,
                         sum_r, sum_x,
                         empty_r, full_r, enr_r, enw_r, dataout_r, datain_r,
                         empty_x, full_x, enr_x, enw_x, dataout_x, datain_x,
                         offset_r, offset_x, reset_col, jp_flgs,
                         jp_lf, jp_sa, jp_rh,
                         col_r, col_x, row_r, row_x, addr_not_reached,
                         dout_rom, addr_rom_r, addr_rom_x, rdy, res_u, noupdate_s,
                         index1_r, index2_r, index3_r, index1_x, index2_x, index3_x)
    instance_7 = jpegfsmupdate(clk_fast, addr0_r, addr0_x, addr1_r, addr1_x,
                               state_r, state_x,
                               dataToRam0_r, dataToRam0_x,
                               dataToRam1_r, dataToRam1_x,
                               dataFromRam0_r, dataFromRam0_x,
                               dataFromRam1_r, dataFromRam1_x,
                               sum_r, sum_x,
                               empty_r, full_r, enr_r, enw_r, dataout_r, datain_r,
                               empty_x, full_x, enr_x, enw_x, dataout_x, datain_x,
                               offset_r, offset_x, col_r, col_x, row_r, row_x,
                               addr_rom_r, addr_rom_x,
                               index1_r, index2_r, index3_r,
                               index1_x, index2_x, index3_x)
    #instance_8 = resetptr(clk_fast, readptr, writeptr, reset_ctn)
    #instance_8 = read_file_sdram(clk_fast, rst, eog, wr_s, rst_file_in, addr_r, dataToRam_r, y)
    instance_8 = rom(dout_rom, addr_rom_r, CONTENT)
    return instance_1, instance_3, instance_5, instance_6, instance_7, instance_8


toVHDL(xess_jpeg_top, clk_fast, addr0_r, addr0_x, addr1_r, addr1_x, state_r, state_x,
       dataToRam0_r, dataToRam0_x, dataFromRam0_x, dataFromRam0_r,
       dataToRam1_r, dataToRam1_x, dataFromRam1_x, dataFromRam1_r,
       sig_in, noupdate_s,
       res_s, res_u, jp_lf, jp_sa ,jp_rh, jp_flgs, reset_col, rdy, addr_not_reached, offset_r, offset_x, dataFromRam0_s,
       done0_s, wr0_s, rd0_s, sum_r, sum_x,
       empty_r, full_r, enr_r, enw_r, dataout_r, datain_r,
       empty_x, full_x, enr_x, enw_x, dataout_x, datain_x,
       col_r, col_x, row_r, row_x,
       dout_rom, addr_rom_r, addr_rom_x, CONTENT, index1_r, index2_r, index3_r, index1_x, index2_x, index3_x)
#toVerilog(rom, dout_rom, addr_rom_r, CONTENT)
 