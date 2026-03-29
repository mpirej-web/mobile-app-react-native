package mobileappreactnative

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"

	"github.com/urfave/cli/v2"
)

func GetProjectDirectory(c *cli.Context) string {
	if c.IsSet("path") {
		return c.String("path")
	} else if currentDir, err := os.Getwd(); err != nil {
		log.Fatal(err)
	} else {
		return currentDir
	}
}

func ValidateProjectName(name string) error {
	if !strings.HasPrefix(name, "mobile-app-") {
		return errors.New("project name must start with 'mobile-app-'")
	}
	if !filepath.ValidPath(name) {
		return errors.New("project name must be a valid path")
	}
	return nil
}

func GenerateProjectName(name string) string {
	if strings.HasPrefix(name, "mobile-app-") {
		return name
	} else {
		return fmt.Sprintf("mobile-app-%s", name)
	}
}

func GetProjectName(path string) (string, error) {
	name := filepath.Base(path)
	if err := ValidateProjectName(name); err != nil {
		return "", err
	}
	return name, nil
}