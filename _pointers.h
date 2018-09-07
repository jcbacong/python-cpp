#pragma once

typedef struct{
	float m,t;
} Point;

extern "C" __declspec(dllexport) void hello_world();
extern "C" __declspec(dllexport) Point* frames(float *a, float *b, int count);
