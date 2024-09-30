#!/bin/bash

echo "Применеие Алембик-миграций..."
alembic upgrade head && exec "$@"